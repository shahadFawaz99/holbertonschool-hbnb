import unittest
from app import create_app

class TestUserEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user_success(self):
        """Test successful user creation"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Alice",
            "last_name": "Smith",
            "email": "alice@example.com"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.get_json())

    def test_create_user_missing_fields(self):
        """Test user creation with missing required fields"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "",
            "last_name": "",
            "email": ""
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_create_user_invalid_email(self):
        """Test user creation with invalid email format"""
        response = self.client.post('/api/v1/users/', json={
            "first_name": "Bob",
            "last_name": "Jones",
            "email": "invalid-email"
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    def test_get_all_users(self):
        """Test retrieving all users"""
        self.client.post('/api/v1/users/', json={
            "first_name": "Test",
            "last_name": "User",
            "email": "test.user@example.com"
        })
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), list)

if __name__ == '__main__':
    unittest.main()

