import csv

def read_csv_input(filename):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)       # csv.reader aus dem csv Modul, gibt alles als eine Liste von str wieder.
            val_arbeitszeiten(reader)
            for row in reader:
                print(row)   # Print each row placeholder for now
                
    #ExceptionHandling
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def val_arbeitszeiten(reader):
    aktuelle_person = None
    pensum = None

    for row in reader:
        row.strip() 

    

# Read File path and call function
csv_file = "data\Berisha, Linda(Alle).csv"
read_csv_input(csv_file)