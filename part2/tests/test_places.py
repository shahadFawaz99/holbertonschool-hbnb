import unittest
from app import create_app
from app.services import facade

class TestPlaceEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        # Create a user to associate with the place
        self.user = facade.create_user({
            "first_name": "Sam",
            "last_name": "Wilson",
            "email": "sam@example.com"
        })

    def test_create_place(self):
        response = self.client.post('/api/v1/places/', json={
            "title": "Cabin Retreat",
            "description": "Quiet and peaceful in the woods",
            "price": 200.0,
            "latitude": 45.0,
            "longitude": -110.0,
            "owner_id": self.user.id
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("Cabin Retreat", response.get_data(as_text=True))

    def test_create_place_invalid_latitude(self):
        response = self.client.post('/api/v1/places/', json={
            "title": "Invalid Latitude",
            "description": "Testing validation",
            "price": 100.0,
            "latitude": 100.0,
            "longitude": 50.0,
            "owner_id": self.user.id
        })
        self.assertEqual(response.status_code, 400)

    def test_get_all_places(self):
        self.client.post('/api/v1/places/', json={
            "title": "Mountain Hut",
            "description": "Snowy views",
            "price": 250.0,
            "latitude": 40.0,
            "longitude": -105.0,
            "owner_id": self.user.id
        })
        response = self.client.get('/api/v1/places/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Mountain Hut", response.get_data(as_text=True))

    def test_update_place(self):
        post_response = self.client.post('/api/v1/places/', json={
            "title": "Old House",
            "description": "Needs renovation",
            "price": 90.0,
            "latitude": 35.0,
            "longitude": -100.0,
            "owner_id": self.user.id
        })
        place_id = post_response.get_json()["id"]

        put_response = self.client.put(f'/api/v1/places/{place_id}', json={
            "title": "Renovated House",
            "price": 120.0
        })
        self.assertEqual(put_response.status_code, 200)
        self.assertIn("Renovated House", put_response.get_data(as_text=True))

    def test_get_place_not_found(self):
        response = self.client.get('/api/v1/places/unknown-id')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()

