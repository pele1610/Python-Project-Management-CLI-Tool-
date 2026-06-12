import json
import os

DATA_DIR = "data"

FILES ={
    "users": os.path.join(DATA_DIR, "users.json"),
    "projects": os.path.join(DATA_DIR, "projects.json"),
    "tasks": os.path.join(DATA_DIR, "tasks.json")
}


def load_data(key: str) -> dict:
    filepath = FILES[key]
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    



def save_data(key: str, data: dict) -> None:
    filepath = FILES[key]
    os.makedirs(DATA_DIR, exist_ok=True)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)