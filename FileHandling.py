import csv

def read_csv(filename):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)   # Print each row
                
    #ExceptionHandling
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Read File path and call function
csv_file = "data\data.csv"
read_csv(csv_file)