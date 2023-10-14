# TODO решите задачу
import json


def task() -> float:
    with open("input.json", 'r') as input_f:
        return round(sum(data["score"] * data["weight"] for data in json.load(input_f)), 3)


print(task())
