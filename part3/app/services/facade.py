from app.services.repositories.user_repository import UserRepository
from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review


class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()

        # These will be migrated to SQLAlchemy in later tasks
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()

    # -------------------- USERS --------------------

    def create_user(self, user_data):
        user = User(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            email=user_data['email']
        )
        user.hash_password(user_data['password'])
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_user_by_email(email)

    def update_user(self, user_id, data):
        user = self.get_user(user_id)
        if not user:
            return None
        if 'email' in data or 'password' in data:
            raise ValueError("Cannot update email or password")
        for key, value in data.items():
            setattr(user, key, value)
        self.user_repo.update(user_id, data)
        return user

    # -------------------- PLACES --------------------

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def create_place(self, place_data, owner_id):
        place = Place(**place_data)
        place.owner_id = owner_id
        self.place_repo.save(place)
        return place

    def update_place(self, place_id, data, user_id):
        place = self.get_place(place_id)
        if not place or place.owner_id != user_id:
            raise PermissionError("Unauthorized action")
        for key, value in data.items():
            setattr(place, key, value)
        self.place_repo.save(place)
        return place

    # -------------------- REVIEWS --------------------

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def create_review(self, review_data, user_id):
        place_id = review_data.get('place_id')
        place = self.get_place(place_id)
        if not place:
            raise ValueError("Place not found")
        if place.owner_id == user_id:
            raise ValueError("Cannot review your own place")
        existing_reviews = self.review_repo.find_by(
            lambda r: r.user_id == user_id and r.place_id == place_id
        )
        if existing_reviews:
            raise ValueError("You have already reviewed this place")
        review = Review(**review_data)
        review.user_id = user_id
        self.review_repo.save(review)
        return review

    def update_review(self, review_id, data, user_id):
        review = self.get_review(review_id)
        if not review or review.user_id != user_id:
            raise PermissionError("Unauthorized action")
        for key, value in data.items():
            setattr(review, key, value)
        self.review_repo.save(review)
        return review

    def delete_review(self, review_id, user_id):
        review = self.get_review(review_id)
        if not review or review.user_id != user_id:
            raise PermissionError("Unauthorized action")
        self.review_repo.delete(review_id)

