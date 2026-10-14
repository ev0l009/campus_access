from utils.helpers import generate_id, generate_user_data

from main import data

def create_user(user):
    name = input("Enter your name: ")
    if not name.strip() or len(name.strip()) < 5:
        raise ValueError("Name canot be empty and must be greater than 5 characters")
    
    password = input("Enter your password: ")
    if not password.strip() or len(password.strip()) < 5:
        raise ValueError("Password canot be empty and must be greater than 5 characters")

    confirmed_password = input("Confirm your password: ")
    if password != confirmed_password:
        raise ValueError("Passwords do not match.")

    id = generate_id(user)

    data["users"][user][id] = generate_user_data(user, id)


def login_user(user):
    id = input("Enter your ID: ")
    password = input("Enter your password: ")

    if id not in data["user"][user]:
        raise ValueError("Invalid ID credentials")

    if password != data["users"][user][id]["password"]:
        raise ValueError("Invalid password credentials")

    return data["user"][user][id]