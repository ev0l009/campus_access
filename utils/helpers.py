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