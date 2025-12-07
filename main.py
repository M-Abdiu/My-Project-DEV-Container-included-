from Input_csv import read_csv_input
from MathBericht import calc_bericht
from Output_csv import csv_output

def main():
    daten = read_csv_input("data/Stempelzeiten_KW_XX.csv")
    bericht = calc_bericht(daten)
    csv_output("data/Auswertung_KW_XX.csv", bericht)

if __name__ == "__main__":
    main()
