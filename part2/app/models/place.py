from app.models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, title, description, price, latitude, longitude, owner_id, amenities=None):
        super().__init__()

        # Validate title
        if not title or len(title) > 100:
            raise ValueError("Invalid title")

        # Validate price
        if price < 0:
            raise ValueError("Price must be a non-negative float")

        # Validate latitude and longitude
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Invalid latitude: must be between -90 and 90")

        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Invalid longitude: must be between -180 and 180")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner_id = owner_id  # Store as owner_id (UUID string)
        self.amenities = amenities if amenities is not None else []  # List of amenity IDs

