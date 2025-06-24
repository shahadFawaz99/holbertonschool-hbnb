
from app.models.base_model import BaseModel

class User(BaseModel):
    def init(self, first_name, last_name, email, is_admin=False):
        super().init()
        if not first_name or len(first_name) > 50:
            raise ValueError("Invalid first name")
        if not last_name or len(last_name) > 50:
            raise ValueError("Invalid last name")
        if not email or "@" not in email:
            raise ValueError("Invalid email")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_admin = is_admin
