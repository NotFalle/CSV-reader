import config.config as cfg
import csv


def search():
    print("Searching!")
    with open('input/contacts.csv', newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for column in reader:
            print(f"{column[1]} {column[2]} - {column[5]} år - tel: '{column[4]}'")


def ping():
    print("Pong!")

def exit():
    print("Exiting!")
    cfg.engine = False