from utils.helpers import generate_id, generate_user_data
from services.storage import save_session

def create_user(user_type, data):
    name = input("Enter your name: ")
    if not name.strip() or len(name.strip()) < 3:
        raise ValueError("Name canot be empty and must be greater than 3 characters")
    
    password = input("Enter your password: ")
    if not password.strip() or len(password) < 4:
        raise ValueError("Password must be greater than 4 characters and canot be empty.")

    confirmed_password = input("Confirm your password: ")
    if password != confirmed_password:
        raise ValueError("Passwords do not match.")

    id = generate_id(user_type)

    data["users"][user_type][id] = generate_user_data(user_type, id, name, password)

    save_session(data)

    print(
        "Registeration successful!\n"
        f"Please note your ID: {id}"
    )

    return "login"


def login_user(user_type, data):
    id = input("Enter your ID: ")
    password = input("Enter your password: ")

    if id not in data["users"][user_type]:
        raise ValueError("Invalid ID credentials")

    if password != data["users"][user_type][id]["password"]:
        raise ValueError("Invalid password credentials")

    return "dashboard", data["users"][user_type][id]