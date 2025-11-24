import json
import os

FILE = "data.json"

def load_data():
    if not os.path.exists(FILE):
        return {"expenses": [], "goals": []}

    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return {"expenses": [], "goals": []}


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data,f,indent=4)