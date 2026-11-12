import objects as obj
import functions as func
import config.config as cfg

## Delete me later
my_dict = {
    "lastsearch": {
        "csvfilename":"contacts.csv", 
        "searchterm":"John"
    }, 
}


func.write_json(my_dict)

data = func.read_json()

while cfg.engine:
    print("hello")
    cfg.hello()
    print(data)
    print("Search term: ", data["lastsearch"]["searchterm"])
    break





