import json

# запись в json
def data_to_json(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        

# чтение из json
def data_from_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
