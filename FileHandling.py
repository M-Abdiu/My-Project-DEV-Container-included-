import csv

def read_csv_input(filename):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)   # Print each row placehgolder for now
                
    #ExceptionHandling
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Read File path and call function
csv_file = "data\input.csv"
read_csv_input(csv_file)