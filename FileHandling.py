import csv


def read_csv_input(filename):  # Funktion zum Lesen des CSV-Dokuments und zum Aufrufen der anderen Funktionen
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            daten = val_arbeitszeiten(reader)
            if daten is not None:
                print("Eingelesene Datenstruktur:")
                print(daten)
                print("-----------------------------------")
            # WICHTIG: Ergebnis zurückgeben
            return daten

    except FileNotFoundError:
        print("Error, Datei nicht gefunden:", filename)
        return None
    except Exception as e:
        print("Es ist ein Fehler aufgetreten: ", e)
        return None


def val_arbeitszeiten(reader):
    mitarbeiter = []
    aktuelle_person = None

    for row in reader:  # leere Zeilen überspringen
        if not row:
            continue

        neue_row = []
        for feld in row:
            neue_row.append(feld.strip())  # Felder von Leerzeichen bereinigen
        row = neue_row

        if len(row) == 0:  # Zeilen ohne Daten ignorieren
            continue

        # Mitarbeiterzeile: Nachname, Vorname, Pensum
        if len(row) == 3 and row[2].isdigit():
            nachname = row[0]
            vorname = row[1]
            pensum = int(row[2])
            mitarbeiter.append([nachname, vorname, pensum, []])
            aktuelle_person = mitarbeiter[-1]

            if pensum < 0 or pensum > 100:
                print("Pensum falsch bei", nachname, vorname, ":", pensum)
                return None

        else:
            # Arbeitszeile ohne vorherige Person
            if aktuelle_person is None:
                print("Arbeitszeile ohne Person:", row)
                return None

            nachname = aktuelle_person[0]
            vorname = aktuelle_person[1]

            tag = row[0]
            wochentage = ("Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag")
            wochenende = ("Samstag", "Sonntag")
            if tag in wochentage:
                pass
            elif tag in wochenende:
                print("ACHTUNG!: ", nachname, vorname, "hat am Wochenendtag:", tag, "gearbeitet!")
                # trotzdem weitergeben
            else:
                print("Tag falsch bei", nachname, vorname, ":", tag)
                return None

            if len(row) != 5:
                print(
                    "Falsche Anzahl Zeit-Einträge bei",
                    nachname,
                    vorname,
                    "am",
                    tag,
                    ", erwartet sind 4 Einträge (Wenn kein Eintrag bitte '00.00' eingeben)",
                )
                return None

            # row = [tag, eintritt, austritt, pause_start, pause_ende]
            aktuelle_person[3].append(row)

            # alle Zeiten in dieser Zeile prüfen
            for zeit in row[1:]:
                if not ist_gueltige_zeit(zeit):
                    print("Zeit falsch bei", nachname, vorname, "am", tag, ":", zeit)
                    return None

    return mitarbeiter


def ist_gueltige_zeit(zeit):  # Check ob Zeiten möglich sind
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

# Methode für Konvertierung der Werte 00.00 in 0.0 Stunden
def zeit_zu_stunden(zeit_str):
    stunden_str, minuten_str = zeit_str.split(".")
    stunden = int(stunden_str)
    minuten = int(minuten_str)
    return stunden + minuten / 60.0


# Methode für Berechnung der Arbeitseinträge der Mitarbeiter + Ausgabe der Werten in Konsole.
def math_stundenrechnung(mitarbeiter):
    #Validierung
    if mitarbeiter is None:
        print("Keine gültigen Mitarbeiterdaten übergeben. Berechnung abgebrochen.")
        return

    for person in mitarbeiter:
        nachname, vorname, pensum, tage = person

        gesamt_effektiv = 0.0
        gesamt_pausen = 0.0

        for tag, eintritt, pause_start, pause_ende, austritt in tage:
            # Zeiten von "HH.MM" in Stunden umrechnen
            eintritt_h = zeit_zu_stunden(eintritt)
            pause_start_h = zeit_zu_stunden(pause_start)
            pause_ende_h = zeit_zu_stunden(pause_ende)
            austritt_h = zeit_zu_stunden(austritt)

            arbeitsstunden = austritt_h - eintritt_h
            pausenstunden = pause_ende_h - pause_start_h
            effektiv = arbeitsstunden - pausenstunden

            gesamt_effektiv += effektiv
            gesamt_pausen += pausenstunden
    


        print(f"{nachname} {vorname} ({pensum}% Pensum):")
        print(f"  Effektive Arbeitsstunden: {gesamt_effektiv:.2f} h")
        print(f"  Pausenstunden gesamt:     {gesamt_pausen:.2f} h")

        verletzung = vertragsbedingungen(gesamt_effektiv, gesamt_pausen, pensum, tag)
        if verletzung:
            print("  -> Vertragsbedingungen: VERLETZT")
            print("  -> Begründung: " + verletzung[1])
        else:
            print("  -> Vertragsbedingungen: OK")
        print()  # Leerzeile zur Trennung
        print("-----------------------------------")    
        print()  # Leerzeile zur Trennung

# Methode für Überprüfung ob Rahmenmbedingungen eines Vertrages gebrochen wurden.
def vertragsbedingungen(gesamt_effektiv, gesamt_pausen, pensum,tag):
    # Max-Werte pro Woche
    max_stunden = 48.0  #Max Stunden Anzahl -> Validierungsvariable
    max_pausen_anzahl = 5.0  #Max Pausen Anzahl -> Validierungsvariable
    
    # Pensum in Prozent
    pensum_faktor = pensum / 100.0
    
    # tuple für Überprüfung von wert variable tag
    wochenende = ("Samstag", "Sonntag")
    
    # Case 1: Effektive Arbeitsstunden sind grösser als Max erlaubte Stunden anhand Pensumfaktor
    if (
        gesamt_effektiv > max_stunden * pensum_faktor
    ):
        begründung = "Unerlaubte Überstunden"
        return True,begründung
    # Case 2: Pausenstunden sind grösser als Max erlaubte Pausen Anzahl
    elif(
        gesamt_pausen > max_pausen_anzahl
    ):
        begründung = "Unerlaubte Pausenstunden"
        return True,begründung
    # Case 3: Variable tag beinhaltet Samstag oder Sonntag
    elif(
        tag in wochenende
    ):
        begründung = "Unerlaubte Wochenendarbeit"
        return True,begründung
    else:
        return False


# Run
if __name__ == "__main__":
    #CSV-Pfad eintragen
    csv_file = input("Bitte Dateinamen eingeben, welche ausgewertet werden soll. (z.B.: Data\ Stempelzeiten KW_XX.csv): ")
    datapoints = read_csv_input(csv_file)

    if datapoints is not None:
        math_stundenrechnung(datapoints)
    else:
        print("Keine Daten eingelesen – keine Berechnung möglich.")
