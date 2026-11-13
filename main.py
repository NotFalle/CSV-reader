#import time
#import objects as obj
import functions as src
import config.config as cfg
import commands
import inspect
import os


def main():

    commands_list = [
        command_name
        for command_name, command_object in vars(commands).items()
        if inspect.isfunction(command_object)
    ]

    try:
        int("Helluuu world")
    except ValueError as e:
        src.save_error(e, os.path.basename(__file__))

    while cfg.engine:

        src.space()

        print("Loaded commands:")
        for _ in commands_list:
            print(f"->  {_}")

        src.space()

        user_input = src.get_user_input("Command: ")

        print(f"You chose: {user_input}")

        break


if __name__ == "__main__":
    print(f"Started main.py!")
    main()
    pass