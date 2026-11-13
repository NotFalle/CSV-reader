import os
import datetime
import json
import config.config as cfg
import modules.generator as gen


# space([i | optional])
def space(i=1):
    for _ in range(i):
        print("")

def timestamp():
    timestamp = datetime.datetime.now().strftime(
        "%H:%M:%S %Y-%m-%d" if cfg.swedish_timestamp
        else "%m/%d/%Y %I:%M:%S %p"
    )
    return timestamp


# crucial_error(msg, e)
def crucial_error(msg, e):
    try:
        print(f"[WARNING]({timestamp()}): {msg} ", e)
        exit()
    except:
        print(f"[WARNING]: {msg} ", e)
        exit()

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

    if location is None and filename is None:
        filepath = os.path.join(
            cfg.default_location,
            f"{gen.string_id()}-{cfg.default_filename}"
        )

    elif location is None and filename is not None:
        filepath = filename

    else:
        if filename is None:
            filename = f"{gen.string_id()}-{cfg.default_filename}"

    return filepath


# check_if_json_exists(filepath)
def check_if_json_exists(filepath): # Check if file exists

    return os.path.isfile(filepath) # Returns if file exist (True or False)


# write_to_json(data, filepath)
def write_to_json(data, filepath):

    with open(filepath, "w", encoding="utf-8") as file: # Creates or overwrites file
        file.write(json.dumps(data) + '\n')


# read_json(filepath)
def read_json(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


# append_to_json(data, filepath)
def append_to_json(data, filepath):

    try:
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(json.dumps(data) + '\n')
    except ValueError as e:
        crucial_error(f"Couldn't append given data to '{filepath}'!", e)


def safe_write_to_json(data, filepath):

    exists = check_if_json_exists(filepath)

    try:
        if exists:
            append_to_json(data, filepath)
        else:
            write_to_json(data, filepath)
    except ValueError as e:
        crucial_error(f"Couldn't write or append data to {filepath}!", e)
