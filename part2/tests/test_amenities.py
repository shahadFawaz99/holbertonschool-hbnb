import unittest
from app import create_app

class TestAmenityEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_amenity(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": "Wi-Fi"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("Wi-Fi", response.get_data(as_text=True))

    def test_create_amenity_invalid(self):
        response = self.client.post('/api/v1/amenities/', json={
            "name": ""
        })
        self.assertEqual(response.status_code, 400)

    def test_get_all_amenities(self):
        self.client.post('/api/v1/amenities/', json={
            "name": "Pool"
        })
        response = self.client.get('/api/v1/amenities/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Pool", response.get_data(as_text=True))

    def test_get_amenity_by_id_not_found(self):
        response = self.client.get('/api/v1/amenities/nonexistent-id')
        self.assertEqual(response.status_code, 404)

    def test_update_amenity(self):
        post_response = self.client.post('/api/v1/amenities/', json={
            "name": "Old Amenity"
        })
        amenity_id = post_response.get_json()["id"]

        put_response = self.client.put(f'/api/v1/amenities/{amenity_id}', json={
            "name": "Updated Amenity"
        })
        self.assertEqual(put_response.status_code, 200)
        self.assertIn("Updated Amenity", put_response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()

