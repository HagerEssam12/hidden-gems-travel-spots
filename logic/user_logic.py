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
 
# Add a travel spot to the user's favorites
def add_favorite(username, spot_id):
    users = load_users()

    for user in users:
        if user["username"] == username:
            # Avoid adding the same spot more than once
            if spot_id not in user["favorites"]:
                user["favorites"].append(spot_id)

            break

    save_users(users)

# Remove a travel spot from the user's favorites
def remove_favorite(username, spot_id):
    users = load_users()

    for user in users:
        if user["username"] == username:
            # Remove the spot if it exists in favorites
            if spot_id in user["favorites"]:
                user["favorites"].remove(spot_id)

            break

    save_users(users)    

# Get the user's favorite spot IDs
def get_user_favorites(username):
    users = load_users()

    for user in users:
        if user["username"] == username:
            return user["favorites"]

    return []    