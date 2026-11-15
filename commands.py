import config.config as cfg
import functions as src
import objects as obj
import csv

temp_csv_file = "input/contacts.csv"

def search():

    src.space(3)
    print(" 1. CSV file must be all lowercase.")
    print(" 2. CSV file must have no spaces.")
    print(" 3. Don't forget '.csv' at the end!")
    src.space()
    user_input = src.get_user_input("CSV filename:")
    print(f"Your entered: '{user_input}'")
    filepath = src.create_filepath(cfg.csv_location, user_input)
    print(f"Searching in '{filepath}'")
    src.space()
    if src.check_if_file_exists(filepath):
        print("Status: Found!")
    else:
        print("Status: No such file by that name.")
    src.space()

    """
    src.space()
    print(f"Avalible columns in '{temp_csv_file}':")
    with open(temp_csv_file, newline="") as csvfile:
        columns = [] # Empty list
        reader = csv.reader(csvfile) # Setting reader to csv file
        columns = next(reader) # Giving columns list all columns
        for _ in columns:
            print(f" - {_}")
    src.space()
    user_input = src.get_user_input("Search in column(s)?", True)
    print(user_input)
    if user_input:
        print("Choose column to add")
    else:
        print("Search:") """

    #chosen_csv_file = obj.csv_file("contacts.csv")

def ping():
    print("Pong!")

def exit():
    print("Exiting!")
    cfg.engine = False