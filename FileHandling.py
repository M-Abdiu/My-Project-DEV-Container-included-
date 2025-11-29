import csv


def read_csv_input(filename):
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            daten = val_arbeitszeiten(reader)
            print(daten)                                   # <--- Ausgabe der kompletten gesammelten Daten
    except FileNotFoundError:
        print("Error, Datei nicht gefunden:", filename)
    except Exception as e:
        print("Es ist ein Fehler aufgetreten:", e)

def val_arbeitszeiten(reader):
    personen = []
    aktuelle_person = None   # Platzhalter

    for row in reader:       # leere Zeilen überspringen
        if not row:
            continue

        neue_row = []                   
        for feld in row:
            neue_row.append(feld.strip())   # felder mit strip() bereinigen
        row = neue_row

        if len(row) == 0:
            continue

        if len(row) == 3 and row[2].isdigit():                   # Mitarbeiterzeile: Nachname, Vorname, Pensum
            nachname = row[0]
            vorname = row[1]
            pensum = int(row[2])
            personen.append([nachname, vorname, pensum, []])  
            aktuelle_person = personen[-1]                    
            if pensum < 0 or pensum > 100:
                print("Pensum falsch bei", aktuelle_person,":", pensum)
        else:
            if aktuelle_person is None:                         # kontrollieren ob es einen Namen gibt
                print("Arbeitszeile ohne Person:", row)
                continue

            tag = row[0]
            WOCHENTAGE = ["Montag","Dienstag","Mittwoch","Donnerstag","Freitag"]
            if tag not in WOCHENTAGE:
                print("Tag falsch bei", aktuelle_person,":", tag)
            
            aktuelle_person[3].append(row)

            for zeit in row[1:]:                                 # alle Zeiten in dieser Zeile prüfen
                if not ist_gueltige_zeit(zeit):
                    print("Zeit falsch bei", aktuelle_person, tag,":", zeit)

    return personen



def ist_gueltige_zeit(zeit):
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