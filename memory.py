import json
import os

MEMORY_FILE = "memory/user_data.json"


def save_memory(data):

    os.makedirs("memory", exist_ok=True)

    with open(MEMORY_FILE, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4
        )


def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return {}

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:

        return json.load(file)