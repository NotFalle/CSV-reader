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
        selected_file = user_input
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

            selected_columns_list = []
            avalible_columns_list = []
            avalible_columns = ""
            selected_columns = ""

            with open(filepath, newline="") as csvfile:
                columns = [] # Empty list
                reader = csv.reader(csvfile) # Setting reader to csv file
                columns = next(reader) # Giving columns list all columns
                for _ in columns:
                    avalible_columns_list.append(_)
            
            user_input = src.get_user_input("Search in column(s)?", True)
            if user_input:
                while True:

                    avalible_columns = ""
                    selected_columns = ""

                    temp_avalible_columns_list = avalible_columns_list
                    temp_selected_columns_list = selected_columns_list

                    avalible_columns_set = set(avalible_columns_list)
                    avalible_columns_list = []
                    for column in columns:
                        if column in avalible_columns_set:
                            avalible_columns_list.append(column)

                    selected_columns_set = set(selected_columns_list)
                    selected_columns_list = []
                    for column in columns:
                        if column in selected_columns_set:
                            selected_columns_list.append(column)
                    
                    for _ in avalible_columns_list:
                        avalible_columns = avalible_columns + f" | {_}"

                    for _ in selected_columns_list:
                        selected_columns = selected_columns + f" | {_}"

                    src.space(10)
                    src.print_header("Selecting columns")
                    src.space(2)
                    print(f"Avalible columns in {selected_file}:")
                    
                    print(avalible_columns + " |")
                    src.space(2)
                    print("Selected columns:")

                    if len(selected_columns_list) == 0:
                        print("None selected.")
                    else:
                        print(selected_columns + " |")
                    src.space(2)

                    entered_column = src.get_user_input("Add/Remove slected column(s):")
                    if entered_column in avalible_columns_list:
                        selected_columns_list.append(entered_column)
                        avalible_columns_list.remove(entered_column)
                    elif entered_column in selected_columns_list:
                        selected_columns_list.remove(entered_column)
                        avalible_columns_list.append(entered_column)

            break


def what_is_saab():
    return "Very great car!"

def help():
    print("Help on the way!")
    return "No help avalible yet..."

def clear():
    print("Clearing!")

def exit():
    print("Exiting!")
    cfg.engine = False