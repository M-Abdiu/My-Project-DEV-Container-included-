#die Auswertung in eine neue CSV-Datei schreiben

import csv

def csv_output(dateiname, bericht):

    header = ["Nachname", "Vorname", "Pensum", "Soll-Zeit", "Ist-Zeit", "Differenz", "Rahemnbedingungen Eingehalten", "Welche Rahmenbedingung vereltzt"]

    with open(dateiname, mode="w", newline="", encoding="utf-8") as datei: 
        writer = csv.writer(datei)

        for eintrag in bericht:
            nachname, vorname, pensum, soll, ist, diff, rahmen_ok, rahmen_text = eintrag        #platzhalten, kommen von Input und Math

            soll_str = f"{soll:.2f}"
            ist_str = f"{ist:.2f}"
            diff_str = f"{diff:+.2f}"  # damit die 2 Nachkommastellen angezeigt werden. und bei der Differenz ein "+" oder "-"


            writer.writerow([nachname, vorname, pensum, soll_str, ist_str, diff_str, rahmen_ok, rahmen_text])


