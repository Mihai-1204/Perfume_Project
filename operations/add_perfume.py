import json

def add_perfume(new_perfume):
    with open("data/perfumes.json", "r") as f:
        perfumes = json.load(f)

    perfumes.append(new_perfume.to_dict())

    with open("data/perfumes.json", "w") as f:
        json.dump(perfumes, f, indent=4)
