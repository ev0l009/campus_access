from utils.validators import get_user_type, get_auth_choice

from utils.validators import get_auth_choice

from services.auth import login_user, create_user

from services.storage import save_session, load_data

def campus_access_runner():
    current_state = "auth_selection"
    auth_type = None
    user_type = None
    user = None
    data = {
        "users": {
            "admin": {},
            "staff": {},
            "student": {},
            "visitor": {}
        },
        "requests": {},
        "cards": {}
    }

    

    while current_state != "exit":

        try:
            data = load_data()
        except Exception as err:
            print(err)
        else:
            print("\nLoading session...\n")
            print(data)

        if current_state == "auth_selection":
            result = get_auth_choice()

            if isinstance(result, tuple):
                current_state, auth_type = result
            else:
                current_state = result

        elif current_state == "role_selection":
            result = get_user_type()

            if isinstance(result, tuple):
                current_state, user_type = result
            elif result == "auth_selection":
                current_state = result
            elif result == "exit":
                current_state = "exit"

        elif current_state == "auth_menu":
            if auth_type == "login":
                result = login_user(user_type, data)
                current_state, user = result

            elif auth_type == "register":
                auth_type = create_user(user_type, data)

        elif current_state == "dashboard":
            print(user)
            break

    try:
        save_session(data)
    except Exception as err:
        print(err)
    else:
        print("Session saved.\n")

    print("Exiting application.")

campus_access_runner()