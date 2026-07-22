class Spot:
    def __init__(self, name, location, category, description, image_url, added_by):
        self.name = name
        self.location = location
        self.category = category
        self.description = description
        self.image_url = image_url
        self.added_by = added_by

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "category": self.category,
            "description": self.description,
            "image_url": self.image_url,
            "added_by": self.added_by
        }

    def short_description(self):
        if len(self.description) > 100:
            return self.description[:100] + "..."
        return self.description