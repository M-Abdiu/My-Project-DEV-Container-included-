import csv


def read_csv_input(filename):                   #Funktion zum lesen des CSV Dokuments und zum aufrufen der anderen Funktionen
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:        #"utf-8" kommt aus dem csv-Modul, zum korrekten Lesen der Daten. 
            reader = csv.reader(file)                                               # .reader kommt ebenfalls direkt als funktion aus dem CSV-Modul 
            daten = val_arbeitszeiten(reader)                                       # 
            if daten is not None:
                print(daten)                                   #Ausgabe der kompletten gesammelten Daten

    except FileNotFoundError:
        print("Error, Datei nicht gefunden:", filename)
    except Exception as e:
        print("Es ist ein Fehler aufgetreten:", e)

def val_arbeitszeiten(reader):
    mitarbeiter = []
    aktuelle_person = None  

    for row in reader:       # leere Zeilen überspringen
        if not row:
            continue

        neue_row = []                   
        for feld in row:
            neue_row.append(feld.strip())    # felder von Leerzeichen bereinigen
        row = neue_row

        if len(row) == 0:                      # Zeilen ohne Daten ignorieren
            continue

        if len(row) == 3 and row[2].isdigit():                   # Mitarbeiterzeile: Nachname, Vorname, Pensum
            nachname = row[0]
            vorname = row[1]
            pensum = int(row[2])
            mitarbeiter.append([nachname, vorname, pensum, []])  
            aktuelle_person = mitarbeiter[-1]  

            if pensum < 0 or pensum > 100:
                print("Pensum falsch bei", nachname, vorname,":", pensum)
                return None
        else:
            if aktuelle_person is None:                         # kontrollieren ob es einen Namen gibt
                print("Arbeitszeile ohne Person:", row)
                return None

            tag = row[0]
            WOCHENTAGE = ("Montag","Dienstag","Mittwoch","Donnerstag","Freitag")
            WOCHENENDE = ("Samstag", "Sonntag")
            if tag in WOCHENTAGE:
                pass
            
            elif tag in WOCHENENDE:
                print("ACHTUNG!: ",  nachname, vorname, "hat am Wochenendtag:", tag, "gearbeitet!")
                pass                                                                                 #Auch wenn am Wochenende gearbeiet wurde, werden die Zeiten weitergegeben, damit man dies in der Überprüfung der Rahmenbedingungen anmerken kann. 

            else:
                print("Tag falsch bei",  nachname, vorname,":", tag) 
                return None
            
            if len(row) != 5: 
                print("Flasche Anzahl Zeit-Einträge bei",  nachname, vorname, "am", tag, ",erwartet sind 4 Einträge (Wenn kein Eintrag bitte '00.00' eingeben)")
                return None
            
            aktuelle_person[3].append(row)

            for zeit in row[1:]:                                 # alle Zeiten in dieser Zeile prüfen
                if not ist_gueltige_zeit(zeit):
                    print("Zeit falsch bei",  nachname, vorname, "am", tag,":", zeit)
                    return None

    return mitarbeiter



def ist_gueltige_zeit(zeit):                #Check ob Zeiten möglich sind 
    teile = zeit.split(".")
    if len(teile) != 2:
        return False
    if not teile[0].isdigit() or not teile[1].isdigit():
        return False
    stunden = int(teile[0])
    minuten = int(teile[1])
    if stunden < 0 or stunden > 23:
        return False
    if minuten < 0 or minuten > 59:
        return False
    return True

csv_file = r"data\Stempelzeiten KW_XX.csv"
read_csv_input(csv_file)

