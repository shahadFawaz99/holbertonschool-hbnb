

from app.models.base_model import BaseModel

class Amenity(BaseModel):
    def init(self, name):
        super().init()
        if not name or len(name) > 50:
            raise ValueError("Invalid amenity name")
        self.name = name

