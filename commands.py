import config.config as cfg
import functions as src
import objects as obj
import csv

temp_csv_file = "input/contacts.csv"

def search():
    src.space()
    print(f"Avalible columns in '{temp_csv_file}':")
    with open(temp_csv_file, newline="") as csvfile:
        columns = [] # Empty list
        reader = csv.reader(csvfile) # Setting reader to csv file
        columns = next(reader) # Giving columns list all columns
        for _ in columns:
            print(f" - {_}")

    #chosen_csv_file = obj.csv_file("contacts.csv")

def ping():
    print("Pong!")

def exit():
    print("Exiting!")
    cfg.engine = False