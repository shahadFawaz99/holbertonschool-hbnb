from app.services.repositories.user_repository import UserRepository
from app.services.repositories.place_repository import PlaceRepository
from app.services.repositories.review_repository import ReviewRepository
from app.services.repositories.amenity_repository import AmenityRepository

from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.user_repo = UserRepository()
        self.place_repo = PlaceRepository()
        self.review_repo = ReviewRepository()
        self.amenity_repo = AmenityRepository()

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

    def create_place(self, place_data):
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def update_place(self, place_id, data):
        self.place_repo.update(place_id, data)
        return self.place_repo.get(place_id)

    def delete_place(self, place_id):
        self.place_repo.delete(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    # -------------------- REVIEWS --------------------

    def create_review(self, review_data):
        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def update_review(self, review_id, data):
        self.review_repo.update(review_id, data)
        return self.review_repo.get(review_id)

    def delete_review(self, review_id):
        self.review_repo.delete(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    # -------------------- AMENITIES --------------------

    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def update_amenity(self, amenity_id, data):
        self.amenity_repo.update(amenity_id, data)
        return self.amenity_repo.get(amenity_id)

    def delete_amenity(self, amenity_id):
        self.amenity_repo.delete(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

