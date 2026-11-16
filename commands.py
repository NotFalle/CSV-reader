import config.config as cfg
import functions as src
import objects as obj
import csv

temp_csv_file = "input/contacts.csv"


def search():

    while True:
        continue_search = False
        
        src.space(10)
        src.print_header("Finding csv file")
        src.space(2)
        print(" 1. CSV file must be all lowercase.")
        print(" 2. CSV file must have no spaces.")
        print(" 3. Don't forget '.csv' at the end!")
        src.space()
        user_input = src.get_user_input("CSV filename:")
        print(f"Searching for: '{user_input}' in '{cfg.csv_location}'")
        filepath = src.create_filepath(cfg.csv_location, user_input)
        src.space()

        if src.check_if_file_exists(filepath):
            print("Status: Found!")
            user_continue = src.get_user_input("Continue?", True)
            if user_continue:
                src.space()
                continue_search = True
                print("Continuing!!")
            else:
                user_try_again = src.get_user_input("Try again?", True)
                if not user_try_again:
                    break
        else:
            print("Status: No such file by that name.")
            user_try_again = src.get_user_input("Try again?", True)
            if not user_try_again:
                break

        # If continue_search is True
        if continue_search:

            selected_columns = []
            user_input = src.get_user_input("Search in column(s)?", True)
            if user_input:
                while True:
                    src.space(10)
                    src.print_header("Selecting columns")
                    src.space(2)
                    print(f"Avalible columns in '{filepath}':")
                    with open(filepath, newline="") as csvfile:
                        columns = [] # Empty list
                        reader = csv.reader(csvfile) # Setting reader to csv file
                        columns = next(reader) # Giving columns list all columns
                        for _ in columns:
                            print(f" - {_}")
                    print("Selected columns:")
                    print(columns)

                    print("Select column(s):")
                    break
            break



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