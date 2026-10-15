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

    default_data = {
        "users": {
            "admin": {},
            "staff": {},
            "student": {},
            "visitor": {}
        }
    }

    if not DB_FILE_PATH.exists() or DB_FILE_PATH.stat().st_size == 0:
        print("New database initialized")
        save_session(default_data)
        return default_data

    try:
        with open(DB_FILE_PATH, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("")
        save_session(default_data)
        return default_data