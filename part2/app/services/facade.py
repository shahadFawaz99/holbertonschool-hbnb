from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place
from app.models.review import Review
from app.models.amenity import Amenity


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # === USER LOGIC ===
    def create_user(self, user_data):
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        return self.user_repo.get(user_id)

    def get_user_by_email(self, email):
        return self.user_repo.get_by_attribute('email', email)

    def get_all_users(self):
        return self.user_repo.get_all()

    def update_user(self, user_id, user_data):
        user = self.user_repo.get(user_id)
        if not user:
            return None

        user.validate()
        if 'first_name' in user_data:
            user.first_name = user_data['first_name']
        else:
            raise TypeError('first_name must be in payload')

        if 'last_name' in user_data:
            user.last_name = user_data['last_name']
        else:
            raise TypeError('last_name must be in payload')

        if 'email' in user_data:
            user.email = user_data['email']
        else:
            raise TypeError('email must be in payload')

        self.user_repo.update(user_id, user)
        return user

    # === PLACE LOGIC ===
    def create_place(self, place_data):
        owner = self.user_repo.get(place_data['owner_id'])
        if not owner:
            raise ValueError("Invalid owner_id")
        place = Place(**place_data)
        self.place_repo.add(place)
        return place

    def get_place(self, place_id):
        return self.place_repo.get(place_id)

    def get_all_places(self):
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            return None
        for key, value in place_data.items():
            if hasattr(place, key):
                setattr(place, key, value)
        self.place_repo.update(place_id, place)
        return place

    # === AMENITY LOGIC ===
    def create_amenity(self, amenity_data):
        amenity = Amenity(**amenity_data)
        self.amenity_repo.add(amenity)
        return amenity

    def get_amenity(self, amenity_id):
        return self.amenity_repo.get(amenity_id)

    def get_all_amenities(self):
        return self.amenity_repo.get_all()

    def update_amenity(self, amenity_id, amenity_data):
        amenity = self.amenity_repo.get(amenity_id)
        if amenity:
            for key, value in amenity_data.items():
                if hasattr(amenity, key):
                    setattr(amenity, key, value)
            self.amenity_repo.update(amenity_id, amenity)
        return amenity

    # === REVIEW LOGIC (Task 5) ===
    def create_review(self, review_data):
        user = self.user_repo.get(review_data['user_id'])
        if not user:
            raise ValueError("Invalid user_id")

        place = self.place_repo.get(review_data['place_id'])
        if not place:
            raise ValueError("Invalid place_id")

        rating = review_data.get('rating')
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Rating must be an integer between 1 and 5")

        review = Review(**review_data)
        self.review_repo.add(review)
        return review

    def get_review(self, review_id):
        return self.review_repo.get(review_id)

    def get_all_reviews(self):
        return self.review_repo.get_all()

    def get_reviews_by_place(self, place_id):
        return [
            review for review in self.review_repo.get_all()
            if review.place_id == place_id
        ]

    def update_review(self, review_id, review_data):
        review = self.review_repo.get(review_id)
        if not review:
            return None
        for key, value in review_data.items():
            if hasattr(review, key):
                setattr(review, key, value)
        self.review_repo.update(review_id, review)
        return review

    def delete_review(self, review_id):
        review = self.review_repo.get(review_id)
        if not review:
            return False
        self.review_repo.delete(review_id)
        return True

