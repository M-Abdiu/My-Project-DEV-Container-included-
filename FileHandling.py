import csv


def read_csv_input(filename): 
    """
    Diese Funktion ist dazu da, das File, welches sich im Dateipfad der Eingabe befindet, versuchen zu öffnen.
    Auch wird die Funktion zur Validierung der Zeit (ob alles korrekt eingegeben wurde) aufgerufen 
    und es wird wiedergegeben, ob es einen Fehler beim Aufruf gibt oder nicht.  
    """

    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            daten = val_arbeitszeiten(reader)
            if daten is not None:
                print("-----------------------------------")
                print("Eingelesene Datenstruktur:")
                print(daten)
                print("-----------------------------------")

            return daten

    except FileNotFoundError:
        print("Error, Datei nicht gefunden:", filename)
        return None
    except Exception as e:
        print("Es ist ein Fehler aufgetreten: ", e)
        return None


def val_arbeitszeiten(reader):
    """
    Diese Funktion validiert, ob die eingelesenen Daten, Fehler enthalten 
    und gibt, falls ein Fehler aufkommt, zurück wo der Fehler liegt.
    Die kontrollierten Werte werden direkt in Listen gespeichert, 
    damit man sie nachher in der Berechnung verwenden kann. 
    Eine weitere Funktion, zur genaueren Überprüfung der Zeitangaben wird aufgerufen.  
    """
    mitarbeiter = []
    aktuelle_person = None
    WOCHENTAGE = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag")
    WOCHENENDE = ("Samstag", "Sonntag")

    for row in reader:
        if not row:
            continue

        neue_row = []
        for feld in row:
            neue_row.append(feld.strip())
        row = neue_row

        if len(row) == 0:
            continue

        if len(row) == 3 and row[2].isdigit():                 # Mitarbeiterzeile: Nachname, Vorname, Pensum
            nachname = row[0]
            vorname = row[1]
            pensum = int(row[2])
            mitarbeiter.append([nachname, vorname, pensum, []])
            aktuelle_person = mitarbeiter[-1]

            if pensum < 0 or pensum > 100:
                print("Pensum falsch bei", nachname, vorname, ":", pensum)
                return None

        else:
            if aktuelle_person is None:
                print("Arbeitszeile ohne Person:", row)
                return None

            nachname = aktuelle_person[0]
            vorname = aktuelle_person[1]

            tag = row[0]


            if tag in WOCHENTAGE:
                pass
            elif tag in WOCHENENDE:                                      # Auch wenn am Wochenende gearbeitet wurde, Werte weitergeben!
                print()             
                print("ACHTUNG!: ", nachname, vorname, "hat am Wochenendtag:", tag, "gearbeitet!") 
                print()  

            else:
                print("Tag falsch bei", nachname, vorname, ":", tag)
                return None

            if len(row) != 5:
                print("Falsche Anzahl Zeit-Einträge bei", nachname, vorname, "am", tag, ", erwartet sind 4 Einträge (Wenn kein Eintrag bitte '00.00' eingeben)")
                
                return None

            tag, eintritt, pause_start, pause_ende, austritt = row
            aktuelle_person[3].append([tag, eintritt, pause_start, pause_ende, austritt])

            zeiten = [eintritt, pause_start, pause_ende, austritt]

            for zeit in zeiten:
                if not ist_gueltige_zeit(zeit):
                    print("Zeit falsch bei", nachname, vorname, "am", tag, ":", zeit)
                    return None

            
            if (pause_start == "00.00") != (pause_ende == "00.00"):
                print("Pause unvollständig bei", nachname, vorname, "am", tag)
                return None  
            
            if eintritt == "00.00" and not (pause_start == "00.00" and pause_ende == "00.00" and austritt == "00.00"):
                print("Eintritt fehlt bei", nachname, vorname, "am", tag)
                return None
            
            if austritt == "00.00" and eintritt != "00.00":
                print("Austritt fehlt bei", nachname, vorname, "am", tag)
                return None


            letzte = None
            for zeit in zeiten:
                if zeit == "00.00":
                    continue

                if letzte is not None and zeit < letzte:
                    print("Anfangszeit später als Endzeit, bei", nachname, vorname, "am", tag)
                    return None
                
                letzte = zeit



    return mitarbeiter


def ist_gueltige_zeit(zeit):
    """
    Diese Funktion überprüft, dass die Zeiten auch tatsächlich möglich sind 
    und die richtige Länge haben. 
    """
    teile = zeit.split(".")
    if len(teile) != 2:
        return False
    if len(teile[0]) != 2 or len(teile[1]) != 2:
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



def math_stundenrechnung(mitarbeiter):
    """
    Hier werden die übergebenen Daten verrechnet, um auf die Ziel-Werte zu kommen. 
    Die Funktion zeit_zu_stunden wird aufgerufen, um die Zeiten auch miteinander verrechnen zu können. 
    Damit man drucken kann, ob vertraglich abgemachte Rahmenbedingungen verletzt wurden, 
    wird die Funktion vertragsbedingungen aufgerufen.
    Die Übersicht wird in die Konsole gedruckt. 
    """
    if mitarbeiter is None:
        print("Keine gültigen Mitarbeiterdaten übergeben. Berechnung abgebrochen.")
        return

    for person in mitarbeiter:
        nachname, vorname, pensum, tage = person

        gesamt_effektiv = 0.0
        gesamt_pausen = 0.0
        soll_zeit = 0.0
        differenz_std = 0.0

        WOCHENENDE = ("Samstag", "Sonntag")
        hat_wochenende = False

        for tag, eintritt, pause_start, pause_ende, austritt in tage:
            if eintritt == "00.00" and pause_start == "00.00" and pause_ende == "00.00" and austritt == "00.00":
                continue

            if tag in WOCHENENDE:
                hat_wochenende = True

            eintritt_h = zeit_zu_stunden(eintritt)
            pause_start_h = zeit_zu_stunden(pause_start)
            pause_ende_h = zeit_zu_stunden(pause_ende)
            austritt_h = zeit_zu_stunden(austritt)

            arbeitsstunden = austritt_h - eintritt_h
            pausenstunden = pause_ende_h - pause_start_h
            effektiv = arbeitsstunden - pausenstunden

            gesamt_effektiv += effektiv
            gesamt_pausen += pausenstunden
            soll_zeit = 42.0 * pensum / 100
            differenz_std = gesamt_effektiv - soll_zeit
    


        print(f"{nachname} {vorname} ({pensum}% Pensum):")
        print(f"  Effektive Arbeitsstunden: {gesamt_effektiv:.2f} h")
        print(f"  Soll-Zeit:                {soll_zeit:.2f} h")
        if differenz_std > 0.0:
            print(f"  Differenz-Zeit:            +{differenz_std:.2f} h")
        elif differenz_std == 0.0:
            print(f"  Differenz-Zeit:            {differenz_std:.2f} h")
        else:
            print(f"  Differenz-Zeit:            {differenz_std:.2f} h")
        print(f"  Pausenstunden gesamt:      {gesamt_pausen:.2f} h")

        verletzung = vertragsbedingungen(gesamt_effektiv, gesamt_pausen, pensum, hat_wochenende)
        if verletzung:
            print("  -> Vertragsbedingungen: VERLETZT")
            print("  -> Begründung: ")
            print("  ->" , ", ".join(map(str, verletzung[1])))
        else:
            print("  -> Vertragsbedingungen: OK")
        print()
        print("-----------------------------------")    
        print()



def zeit_zu_stunden(zeit_str):
    """
    Damit man mit den Zeiten rechnen kann, werden sie in dieser Funktion, zu Industrie-Stunden verrechnet. 
    """
    stunden_str, minuten_str = zeit_str.split(".")
    stunden = int(stunden_str)
    minuten = int(minuten_str)
    return stunden + minuten / 60.0


def vertragsbedingungen(gesamt_effektiv, gesamt_pausen, pensum, hat_wochenende):
    """
    Diese Funktion ist dazu da, dass man überprüft, ob und welche Rahmenbedingungen verletzt wurden und dies an die Stundenrechnung zurückgeben kann.
    """
    max_stunden = 48.0               #Max Stunden Anzahl -> Validierungsvariable
    max_pausen_anzahl = 5.0          #Max Pausen Anzahl -> Validierungsvariable
    
    pensum_faktor = pensum / 100.0
    

    begründung = [] 

    if gesamt_effektiv > max_stunden * pensum_faktor:
        begründung.append("Unerlaubte Überstunden")

    if gesamt_pausen > max_pausen_anzahl:
        begründung.append("Unerlaubte Pausenstunden")

    if hat_wochenende:
        begründung.append("Unerlaubte Wochenendarbeit")

    if begründung:
        return True, begründung
    
    return False


   



if __name__ == "__main__":

    csv_file = input("Bitte Dateipfad der CSV Datei eingeben, welche ausgewertet werden soll: ")
    datapoints = read_csv_input(csv_file)

    if datapoints is not None:
        print()  
        print()  
        print("Übersicht:")
        print("-----------------------------------")  
        print()  
        math_stundenrechnung(datapoints)
        print("Ende der Liste")
    else:
        print("Keine Daten eingelesen → keine Berechnung möglich.")
