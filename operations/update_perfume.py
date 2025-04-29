import json

def update_perfume(name, updated_info):
    with open("data/perfumes.json", "r") as f:
        perfumes = json.load(f)

    for perfume in perfumes:
        if perfume['name'] == name:
            perfume.update(updated_info)

    with open("data/perfumes.json", "w") as f:
        json.dump(perfumes, f, indent=4)
