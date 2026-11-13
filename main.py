import time
import objects as obj
import functions as src
import config.config as cfg
import commands
import inspect



def main():
    ## Delete me later - TEMPORARY
    my_dict = {
        "lastsearch": {
            "csvfilename":"contacts.csv", 
            "searchterm":"John"
        }, 
    }


    ## TEMPORARY

    src.safe_write_to_json(my_dict, src.create_filepath())

    data = src.read_json()

    # get_user_input(message, [string | optional], [yes_or_no | optional])
    def get_user_input(msg, string=True, yes_or_no=False):

        if yes_or_no:
            while True:
                user_input = input(f"{msg} [y/n]: ").strip().lower()

                try:
                    user_input = str(user_input)
                    if user_input == "y":
                        return True
                    elif user_input == "n":
                        return False
                    else:
                        print("Please only type one letter.")
                
                except ValueError as e:
                    print("Couldn't validate user_input.", e)
                    src.write_to_json(e, cfg.error_log, cfg.error_log_file_name)

        else:
            if string:
                user_input = input(msg)
            else:
                user_input = input(msg)
        
        return user_input



    commands_list = [
        command_name
        for command_name, command_object in vars(commands).items()
        if inspect.isfunction(command_object)
    ]

    try:
        int("Bugging in the beninging :)")

    except ValueError as e:
        print("Couldn't validate user_input.", e)

        src.write_to_json(src.gen_error_message(e, __name__), cfg.error_log, cfg.error_log_file_name)

    while cfg.engine:
        print("Started!")

        src.space()

        print("Loaded commands:")
        for _ in commands_list:
            print(f"->  {_}")

        src.space()

        user_input = get_user_input("Command: ")

        print(f"You chose: {user_input}")

        break





if __name__ == "__main__":
    print(f"Started {__name__}!")
    main()
    pass