from utils.validators import get_user_type, get_auth_choice

data = {
    "users": {},
    "requests": {},
    "cards": {}
}

def campus_access():
    auth_choice = None
    exit = False

    while not auth_choice:
        try:
            auth_choice = get_auth_choice()

            if auth_choice == "exit":
                break

        except ValueError as err:
            print(err)

        while auth_choice:
            user = None

            try:
                user = get_user_type()

                if user == "exit":
                    break

            except ValueError as err:
                print(err)

            while user is not None:
                print(f"_____{auth_choice.upper()}_____")

                if auth_choice == "login":
                    print()

    
campus_access()