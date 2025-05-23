from operations.utils import read_json_file, write_json_file
from perfume import Perfume

DATA_FILE = "data/perfumes.json"


def get_all_perfumes():
    return read_json_file(DATA_FILE)


def add_perfume(perfume: Perfume):
    perfume.validate()
    perfumes = get_all_perfumes()
    for p in perfumes:
        if p['name'].lower() == perfume.name.lower():
            if set(c.lower() for c in p['concentration']) & set(c.lower() for c in perfume.concentration):
                raise ValueError("Perfume already exists in the database with same concentration.")
    perfumes.append(perfume.to_dict())
    write_json_file(DATA_FILE, perfumes)


def update_perfume(name, concentration_value, new_perfume: Perfume):
    new_perfume.validate()
    perfumes = get_all_perfumes()
    for idx, p in enumerate(perfumes):
        if p['name'].lower() == name.lower() and concentration_value.lower() in [c.lower() for c in p['concentration']]:
            perfumes[idx] = new_perfume.to_dict()
            write_json_file(DATA_FILE, perfumes)
            return
    raise ValueError("Perfume not found for update.")


def delete_perfume(name, concentration_value):
    perfumes = get_all_perfumes()
    new_list = [
        p for p in perfumes
        if not (p['name'].lower() == name.lower() and concentration_value.lower() in [c.lower() for c in p['concentration']])
    ]
    if len(new_list) == len(perfumes):
        raise ValueError("Perfume not found for deletion.")
    write_json_file(DATA_FILE, new_list)
