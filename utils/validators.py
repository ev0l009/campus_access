from services.ui import auth_selection_txt, user_selection_txt

def get_auth_choice():
    
    choice = input(auth_selection_txt)

    if choice == "1":
        return ("role_selection", "login")
    elif choice == "2":
            return ("role_selection", "register") 
    elif choice == "3":
        return "exit"
    else:
        raise ValueError("\nInvalid auth choice. Try again\n")

def get_user_type():

    roles = {
        "1": "admin",
        "2": "staff",
        "3": "student",
        "4": "visitor"
    }
    
    choice = input(user_selection_txt)

    if choice == "5":
        return "auth_selection"
    elif choice == "6":
        return "exit"
    elif choice not in roles:
        raise ValueError("\nInvalid user type selection. Try again\n")
    else:
        return ("auth_menu", roles[choice])