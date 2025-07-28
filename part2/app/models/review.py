from app.models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text, rating, user_id, place_id):
        super().__init__()

        if not text or not text.strip():
            raise ValueError("Review text is required")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")
        if not user_id:
            raise ValueError("user_id is required")
        if not place_id:
            raise ValueError("place_id is required")

        self.text = text
        self.rating = rating
        self.user_id = user_id
        self.place_id = place_id

