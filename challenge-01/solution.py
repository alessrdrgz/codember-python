import requests
import re


def validate_user(user_keys):
    valid_keys = ["usr", "eme", "psw", "age", "loc", "fll"]
    for valid_key in valid_keys:
        if valid_key not in user_keys:
            return False
    return True


def get_users():
    r = requests.get("https://codember.dev/users.txt")
    users_file = r.text
    return users_file.split("\n\n")


if __name__ == "__main__":
    users = get_users()
    valid_users = 0
    last_valid_user = None

    for user in users:
        user = user.replace("\n", " ")
        current_keys = []
        current_user = None
        for match in re.findall(r'(\w+):(\S+)?', user):
            key, value = match
            if key == "usr":
                current_user = value
            current_keys.append(key)

        if validate_user(current_keys):
            valid_users += 1
            last_valid_user = current_user

    print(f'Valid users: {valid_users}')
    print(f'Last valid user: {last_valid_user}')
