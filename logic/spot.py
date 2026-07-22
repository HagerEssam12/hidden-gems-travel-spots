class Spot:
    def __init__(self, spot_id, name, description, location, category, image_url, added_by):
        self.id = spot_id
        self.name = name
        self.description = description
        self.location = location
        self.category = category
        self.image_url = image_url
        self.added_by = added_by

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "location": self.location,
            "category": self.category,
            "image_url": self.image_url,
            "added_by": self.added_by
        }

    def short_description(self):
        if len(self.description) > 100:
            return self.description[:100] + "..."
        return self.description