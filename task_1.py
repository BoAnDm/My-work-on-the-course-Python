import json

def task() -> float:
    file_name = "input.json"
    with open(file_name, encoding="utf-8") as f:
        json_data = json.load(f)
    json_sum = 0
    for i in json_data:
        json_sum += i.get("score") * i.get("weight")
    return round(json_sum, 3)
print(task())

