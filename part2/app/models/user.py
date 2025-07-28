from app.models.base_model import BaseModel
import re

class User(BaseModel):
    def __init__(self, first_name, last_name, email):
        super().__init__()

        if not first_name or not first_name.strip():
            raise ValueError("First name is required")
        if not last_name or not last_name.strip():
            raise ValueError("Last name is required")
        if not email or not self._is_valid_email(email):
            raise ValueError("A valid email is required")

        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def _is_valid_email(self, email):
        # Simple regex for validating an email address
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None

