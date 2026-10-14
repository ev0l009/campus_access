from services.ui import auth_txt, welcome_txt

def get_auth_choice():
    auth_choice = {
        "1": "login",
        "2": "register",
        "3": "exit"
    }

    choice = input(auth_txt)

    if choice not in auth_choice:
            raise ValueError("\nInvalid user type selection. Try again\n")

    return auth_choice[choice]

def get_user_type():
    user_types = {
        "1": "admin",
        "2": "staff",
        "3": "student",
        "4": "visitor",
        "5": "exit"
    }

    choice = input(welcome_txt)

    if choice not in user_types:
        raise ValueError("\nInvalid user type selection. Try again\n")

    return user_types[choice]