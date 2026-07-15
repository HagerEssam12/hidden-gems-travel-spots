import json

# Path to the spots JSON file
SPOTS_FILE = "data/spots.json"


# Load all travel spots from the JSON file
def load_spots():
    with open(SPOTS_FILE, "r") as file:
        spots = json.load(file)

    return spots

# Save travel spots to the JSON file
def save_spots(spots):
    with open(SPOTS_FILE, "w") as file:
        json.dump(spots, file, indent=4)

# Add a new travel spot
def add_spot(name, description, location, category, image_url, added_by):
    spots = load_spots()

    # Create a new travel spot
    new_spot = {
        "id": len(spots) + 1,
        "name": name,
        "description": description,
        "location": location,
        "category": category,
        "image_url": image_url,
        "added_by": added_by
    }

    # Add the new spot to the spots list
    spots.append(new_spot)

    # Save the updated spots list
    save_spots(spots)

