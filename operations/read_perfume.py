import json

def read_perfumes(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
