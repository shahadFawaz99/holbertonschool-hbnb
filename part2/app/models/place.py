from app.models.base_model import BaseModel

class Place(BaseModel):
    def init(self, title, description, price, latitude, longitude, owner):
        super().init()
        if not title or len(title) > 100:
            raise ValueError("Invalid title")
        if price < 0:
            raise ValueError("Price must be positive")
        if not (-90.0 <= latitude <= 90.0):
            raise ValueError("Invalid latitude")
        if not (-180.0 <= longitude <= 180.0):
            raise ValueError("Invalid longitude")

        self.title = title
        self.description = description
        self.price = price
        self.latitude = latitude
        self.longitude = longitude
        self.owner = owner
        self.reviews = []
        self.amenities = []

    def add_review(self, review):
        self.reviews.append(review)

    def add_amenity(self, amenity):
        self.amenities.append(amenity)
