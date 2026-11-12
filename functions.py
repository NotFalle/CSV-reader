import os
import datetime
import json
import config.config as cfg

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

def gen_error_message(e):
    error_message = {
        "timestamp": timestamp(),
        "error_type": type(e).__name__,
        "error_message": str(e),
        "function": "main",
        "category": "ValidationError"
    }
    return error_message


# Att göra: ändra json till jsonl för bättre struktur och mindre minnes förbrukning

## Json file stuffy

# create_filepath(location, filename)
def create_filepath(location, filename): # Creates a filepath

    if location is not None:
        os.makedirs(location, exist_ok=True) # Creates a directiore if none
        filepath = os.path.join(location, filename) # Joins given location and filename to create a filepath
    else:
        filepath = filename # Sets filepath to filename if no location is given(will end up in root folder)

    return filepath


# check_if_json_exists([location | optional], [filename | optional])
def check_if_json_exists(filepath): # Check if file exists

    return os.path.isfile(filepath) # Returns if file exist (True or False)


# write_to_json(data, [location | optional], [filename | optional])
def write_to_json(data, location=None, filename=cfg.filename):

    filepath = create_filepath(location, filename)

    with open(filepath, "w", encoding="utf-8") as f: # Opens and writes in file
        json.dump(data, f, indent=4)


# read_json()
def read_json():
    with open(cfg.filename, "r", encoding="utf-8") as f:
        return json.load(f)


# append_to_json(data, [location | optional], [filename | optional])
def append_to_json(data, location=None, filename=cfg.filename):
    
    filepath = create_filepath(location, filename)

    file_exists = check_if_json_exists(filepath)

    if file_exists:
        with open(filepath, "a", encoding="utf-8") as f:
            f.write("\n")
            json.dump(data, f, indent=4)
    else:
        write_to_json(data, location, filename)




