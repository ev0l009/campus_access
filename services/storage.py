from pathlib import Path
import json

DB_DIR = Path(__file__).resolve().parent.parent/"data"
DB_FILE_PATH = DB_DIR/"data.json"

def save_session(data):

    try:
        with open(DB_FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)
    except (json.JSONDecodeError, PermissionError) as err:
        raise 

def load_data():
    DB_DIR.mkdir(parents=True, exist_ok=True)

    try:
        with open(DB_FILE_PATH, "r") as file:
            raw_data = json.load(file)
    except:
        raise
    else:
        return raw_data