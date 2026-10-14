import string
import secrets

def generate_id(user_type):
    preffix = {
        "admin": "adm",
        "staff": "stf",
        "student": "std",
        "visitor": "vst"
    }

    pool = string.ascii_letters + string.digits
    suffix = secrets.choice(pool for _ in range(3))
    return f"{preffix[user_type]}_{suffix}"

def generate_user_data(user_type, user_id):
    if user_type == "admin":
        return {
                "adm_id": user_id,
                "name": "",
                "password": "",
                "approved_requests_id": [],
                "issued_card_ids": []
            }
    elif user_type == "staff":
        return {
                "stf_id": user_id,
                "name": "",
                "password": "",
                "issued_card_id": "",
                "created_requests_id": [],
                "approved_requests_id": [],
                "issued_card": ""
            }
    elif user_type == "student":
        return {
                "stf_id": user_id,
                "name": "",
                "password": "",
                "created_requests_id": [],
                "issued_card_id": "",
                "issued_card": ""
            }
    elif user_type == "visitor":
        return {
                "vst_id": user_id,
                "name": "",
                "password": "",
                "created_requests_id": [],
                "issued_card_id": "",
                "issued_card": ""
            }