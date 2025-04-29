import json

def delete_perfume(name):
    with open("data/perfumes.json", "r") as f:
        perfumes = json.load(f)

    perfumes = [perfume for perfume in perfumes if perfume['name'] != name]

    with open("data/perfumes.json", "w") as f:
        json.dump(perfumes, f, indent=4)
