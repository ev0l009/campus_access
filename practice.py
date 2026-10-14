welcome_txt = (
    
    "Who are you?\n"
    "1. Admin\n"
    "2. Staff\n"
    "3. Student\n"
    "4. Visitor\n"
    "5. Exit\n"
    "_____________________________________\n"
    "Select an option: "
)

auth_txt = (
    "\n======= Campus Access =======\n"
    "------ Authentication ------\n"
    "1. Login\n"
    "2. Register\n"
    "3. Exit\n"
)

admin_menu = (
    "====== "
)

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
                print(f"{auth_choice.upper()}")
                break

            



        

    

campus_access()

{   
    "users" :{
        "admins": {
            "adm_id": {
                "adm_id": "",
                "name": "",
                "approved_requests_id": [],
                "issued_card_ids": []
            }
        }, 
        "staff": {
            "stf_id": {
                "stf_id": "",
                "name": "",
                "issued_card_id": "",
                "created_requests_id": [],
                "approved_requests_id": [],
                "issued_card": ""
            }
        },
        "student": {
            "stf_id": {
                "stf_id": "",
                "name": "",
                "created_requests_id": [],
                "issued_card_id": "",
                "issued_card": ""
            }
        },
        "visitors": {
            "vst_id": {
                "vst_id": "",
                "name": "",
                "created_requests_id": [],
                "issued_card_id": "",
                "issued_card": ""
            }
        },
    },
    "requests": {
        "rqt_id": {
            "rqt_id": "",
            "requester_id": "",
            "card_type": "",
            "status": "requested",
            "approved_by": ""
        }
    },
    "cards": {
        "crd_id": {
            "rqt_id": "",
            "card_type": "",
            "card_status": "",
            "issued_to": "",
            "approved_by": ""
        }
    }
}