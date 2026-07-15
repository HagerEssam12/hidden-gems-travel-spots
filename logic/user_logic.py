import json

# Path to the users JSON file
USERS_FILE = "data/users.json"

# Load all users from the JSON file
def load_users():
    with open(USERS_FILE, "r") as file:
        users = json.load(file)

    return users

# Save users to the JSON file
def save_users(users):
    with open(USERS_FILE, "w") as file:
        json.dump(users, file, indent=4)   

# Check if a username already exists
def user_exists(username):
    users = load_users()

    for user in users:
        if user["username"] == username:
            return True

    return False        

# Add a new user
def add_user(username, password):
    users = load_users()

    # Create a new user
    new_user = {
        "username": username,
        "password": password,
        "favorites": []
    }

    # Add the new user to the users list
    users.append(new_user)

    # Save the updated users list
    save_users(users)

# Check user login credentials
def validate_user(username, password):
    users = load_users()

    for user in users:
        if user["username"] == username and user["password"] == password:
            return True

    return False    