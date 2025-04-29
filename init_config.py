import json

def load_config(file_path="config/config.json"):
    with open(file_path, "r") as f:
        return json.load(f)
