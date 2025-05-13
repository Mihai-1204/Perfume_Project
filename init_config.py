import json

def load_config(path='config/config.json'):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Configuration file {path} not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Configuration file {path} is corrupted.")
        return {}
