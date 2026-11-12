import json
import config.config as cfg




def write_json(data):
    with open(cfg.filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def read_json():
    with open(cfg.filename, "r", encoding="utf-8") as f:
        return json.load(f)