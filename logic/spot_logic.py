import json
from logic.spot import Spot

# Path to the travel spots JSON file
SPOTS_FILE = "data/spots.json"
# Path to the travel spots JSON file
SPOTS_FILE = "data/spots.json"


# Load all travel spots from the JSON file
def load_spots():
    with open(SPOTS_FILE, "r") as file:
        spots = json.load(file)

    return spots


# Save the updated travel spots list to the JSON file
def save_spots(spots):
    with open(SPOTS_FILE, "w") as file:
        json.dump(spots, file, indent=4)


# Add a new travel spot
def add_spot(name, description, location, category, image_url, added_by):
    spots = load_spots()

    # Generate a unique ID for the new spot
    new_id = max([spot["id"] for spot in spots], default=0) + 1

    # Create a Spot object
    new_spot = Spot(
        new_id,
        name,
        description,
        location,
        category,
        image_url,
        added_by
    )

    # Convert the object to a dictionary
    spots.append(new_spot.to_dict())

    save_spots(spots)


# Search and filter travel spots
def filter_spots(spots, search_query="", category=""):
    filtered_spots = []

    for spot in spots:

        # Check if the search text matches the spot name or location
        matches_search = (
            search_query.lower() in spot["name"].lower()
            or search_query.lower() in spot["location"].lower()
        )

        # Check if the selected category matches
        matches_category = (
            category == ""
            or spot["category"] == category
        )

        # Add the spot if it matches both conditions
        if matches_search and matches_category:
            filtered_spots.append(spot)

    return filtered_spots


# Delete a travel spot by its ID
def delete_spot(spot_id):
    spots = load_spots()

    spots = [
        spot for spot in spots
        if spot["id"] != spot_id
    ]

    save_spots(spots)


# Return a travel spot using its ID
def get_spot_by_id(spot_id):
    spots = load_spots()

    for spot in spots:
        if int(spot["id"]) == int(spot_id):
            return spot

    return None


# Edit an existing travel spot
def edit_spot(spot_id, updated_data):
    spots = load_spots()

    for spot in spots:
        if spot["id"] == spot_id:
            spot["name"] = updated_data["name"]
            spot["description"] = updated_data["description"]
            spot["location"] = updated_data["location"]
            spot["category"] = updated_data["category"]
            spot["image_url"] = updated_data["image_url"]
            break

    save_spots(spots)