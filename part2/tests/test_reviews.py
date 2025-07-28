import unittest
from app import create_app
from app.services import facade

class TestReviewEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        # Create user and place for review association
        self.user = facade.create_user({
            "first_name": "Alice",
            "last_name": "Smith",
            "email": "alice@example.com"
        })

        self.place = facade.create_place({
            "title": "Beach House",
            "description": "Cozy place near the beach",
            "price": 150.0,
            "latitude": 36.5,
            "longitude": -120.0,
            "owner_id": self.user.id
        })

    def test_create_review(self):
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Beautiful place!",
            "rating": 5,
            "user_id": self.user.id,
            "place_id": self.place.id
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("Beautiful place!", response.get_data(as_text=True))

    def test_create_review_invalid_rating(self):
        response = self.client.post('/api/v1/reviews/', json={
            "text": "Invalid rating",
            "rating": 7,
            "user_id": self.user.id,
            "place_id": self.place.id
        })
        self.assertEqual(response.status_code, 400)

    def test_get_all_reviews(self):
        self.client.post('/api/v1/reviews/', json={
            "text": "Nice view",
            "rating": 4,
            "user_id": self.user.id,
            "place_id": self.place.id
        })
        response = self.client.get('/api/v1/reviews/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Nice view", response.get_data(as_text=True))

    def test_update_review(self):
        post_response = self.client.post('/api/v1/reviews/', json={
            "text": "Just okay",
            "rating": 3,
            "user_id": self.user.id,
            "place_id": self.place.id
        })
        review_id = post_response.get_json()["id"]

        put_response = self.client.put(f'/api/v1/reviews/{review_id}', json={
            "text": "Actually very nice",
            "rating": 5
        })
        self.assertEqual(put_response.status_code, 200)

    def test_delete_review(self):
        post_response = self.client.post('/api/v1/reviews/', json={
            "text": "Short stay",
            "rating": 2,
            "user_id": self.user.id,
            "place_id": self.place.id
        })
        review_id = post_response.get_json()["id"]

        delete_response = self.client.delete(f'/api/v1/reviews/{review_id}')
        self.assertEqual(delete_response.status_code, 200)

    def test_get_reviews_by_place(self):
        self.client.post('/api/v1/reviews/', json={
            "text": "Peaceful atmosphere",
            "rating": 5,
            "user_id": self.user.id,
            "place_id": self.place.id
        })
        response = self.client.get(f'/api/v1/places/{self.place.id}/reviews')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Peaceful atmosphere", response.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()

