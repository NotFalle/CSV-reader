import os
import datetime
import json
import config.config as cfg
import modules.generator as gen


# space([i | optional])
def space(i=1):
    for _ in range(i):
        print("")

# timestamp()
def timestamp():
    timestamp = datetime.datetime.now().strftime(
        "%H:%M:%S %Y-%m-%d" if cfg.swedish_timestamp
        else "%m/%d/%Y %I:%M:%S %p"
    )
    return timestamp


## Error handeling stuffy

# crucial_error(msg, e)
def crucial_error(msg, e):
    try:
        print(f"[WARNING]({timestamp()}): {msg} ", e)
        exit()
    except:
        print(f"[WARNING]: {msg} ", e)
        exit()

# gen_error_message(e, filename)
def gen_error_message(e, filename):
    try:
        error_message = {
            "timestamp": timestamp(),
            "error_type": type(e).__name__,
            "error_message": str(e),
            "function": str(filename),
            "category": "ValidationError"
        }
        return error_message
    except ValueError as e:
        crucial_error("Couldn't create format error data!", e)


## json file stuffy

# create_filepath(location, filename)
def create_filepath(location=None, filename=None): # Creates a filepath

    if location is None and filename is None: # If no location and no filename
        os.makedirs(cfg.default_location, exist_ok=True) # Create directory
        filepath = os.path.join(
            cfg.default_location,
            f"{gen.string_id()}-{cfg.default_filename}"
        ) # Sets filepath

    elif location is None and filename is not None: # If no loction but filename
        filepath = filename # location is set to filename

    else: # If location is given
        if filename is None: # And filename is not
            filename = f"{gen.string_id()}-{cfg.default_filename}" # Sets default filename

        os.makedirs(location, exist_ok=True) # Create directory
        filepath = os.path.join(
            location,
            filename
        ) # Sets filepath
        
    # This way create_filepath() uses config.py if no arguments are given.

    return filepath # Returns value

# check_if_json_exists(filepath)
def check_if_json_exists(filepath): # Check if file exists

    return os.path.isfile(filepath) # Returns if file exist (True or False)

# write_to_json(data, filepath)
def write_to_json(data, filepath):

    with open(filepath, "w", encoding="utf-8") as file: # Creates or overwrites file
        file.write(json.dumps(data) + '\n')

# read_json(filepath)
def read_json(filepath):
    exists = check_if_json_exists(filepath)
    if exists:
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                return json.load(file)
        except ValueError as e:
            crucial_error(f"Couldn't read {filepath}!", e)
    else:
        print(f"{filepath} doesn't exist!")

# append_to_json(data, filepath)
def append_to_json(data, filepath):

    try:
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(json.dumps(data) + '\n')
    except ValueError as e:
        crucial_error(f"Couldn't append given data to '{filepath}'!", e)

# safe_write_to_json(data, filepath)
def safe_write_to_json(data, filepath):

    exists = check_if_json_exists(filepath)

    try:
        if exists:
            append_to_json(data, filepath)
        else:
            write_to_json(data, filepath)
    except ValueError as e:
        crucial_error(f"Couldn't write or append data to {filepath}!", e)


# Error handling writing to file (using functions above)
def save_error(e, filename): # save_error(e, filename)
    msg = gen_error_message(e, filename)
    filepath = create_filepath(cfg.error_log_location, cfg.error_log_filename)
    safe_write_to_json(msg, filepath)


## User related stuffy

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
                save_error(e, os.path.basename(__file__))
    else:
        if string:
            user_input = input(msg)
        else:
            user_input = input(msg)
    return user_input







