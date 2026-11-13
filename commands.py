import config.config as cfg
import objects as obj
import csv


def search():
    print("Searching!")
    with open('input/contacts.csv', newline="") as csvfile:
        columns = [] # Empty list
        reader = csv.reader(csvfile) # Setting reader to csv file
        columns = next(reader) # Giving columns list all columns
        for column in reader: # Going trough the rest of the file
            columns.append(column)
            print(f"{column[1]} {column[2]} - {column[5]} år - tel: '{column[4]}'")

    #chosen_csv_file = obj.csv_file("contacts.csv")

def ping():
    print("Pong!")

def exit():
    print("Exiting!")
    cfg.engine = False