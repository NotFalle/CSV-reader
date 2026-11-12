import objects as obj
import functions as func
import config.config as cfg
import commands
import inspect

## Delete me later - TEMPORARY
my_dict = {
    "lastsearch": {
        "csvfilename":"contacts.csv", 
        "searchterm":"John"
    }, 
}


## TEMPORARY

func.write_json(my_dict)

data = func.read_json()

# get_user_input([message | optional], [string | optional], [yes_or_no | optional])
def get_user_input(msg=None, string=True, yes_or_no=False):

    if yes_or_no:
        if msg == None:
            user_input = input("Message [y/n]: ")
        else:
            user_input = input(msg)
    else:
        if string:
            if msg == None:
                user_input = input("Command: ")
            else:
                user_input = input(msg)
        else:
            if msg == None:
                user_input = input("Enter an number: ")
            else:
                user_input = input(msg)
    
    return user_input



commands_list = [
    command_name for command_name, command_object in inspect.getmembers(commands, inspect.isfunction)
]



while cfg.engine:
    print("Started!")

    func.space()

    print("Loaded commands:")
    for _ in commands_list:
        print(f"->  {_}")

    func.space()

    print(get_user_input())


    break





