import json
import config.config as cfg

# space([i | optional])
def space(i=1):
    for _ in range(i):
        print("")

# write_json(data)
def write_json(data):
    with open(cfg.filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

# read_json()
def read_json():
    with open(cfg.filename, "r", encoding="utf-8") as f:
        return json.load(f)