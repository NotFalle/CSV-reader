#import time
#import objects as obj
import functions as src
import config.config as cfg
import commands
import inspect


def main():

    commands_list = [
        command_name
        for command_name, command_object in vars(commands).items()
        if inspect.isfunction(command_object)
    ]

    while cfg.engine:

        src.space()

        print("Loaded commands:")
        for _ in commands_list:
            print(f"->  {_}")

        src.space()

        user_input = get_user_input("Command: ")

        print(f"You chose: {user_input}")

        break


if __name__ == "__main__":
    print(f"Started main.py!")
    main()
    pass