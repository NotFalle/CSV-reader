import objects as obj
import functions as func
import config.config as cfg

## Delete me later
my_dict = {"name": "Alice", "age": 30, "is_active": True}


func.write_json(my_dict)

data = func.read_json()

while cfg.engine:
    print("hello")
    cfg.hello()
    print(data)
    print("Name: ", data["name"])
    break





