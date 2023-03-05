import unittest
from unittest.mock import patch

from app import create_app


class TestAuthViews(unittest.TestCase):
    def setUp(self):
        self.app = create_app(testing=True)
        self.client = self.app.test_client()
        self.base_url = '/auth'

    def test_register_user(self):
        # Given
        data = {
            "email": "testuser@test.com",
            "password": "password123",
            "name": "Test User"
        }
        expected_status = 201

        # When
        response = self.client.post(f"{self.base_url}/register", json=data)

        # Then
        self.assertEqual(response.status_code, expected_status)

    def test_login(self):
        # Given
        data = {
            "email": "testuser@test.com",
            "password": "password123"
        }
        expected_status = 200

        # When
        response = self.client.post(f"{self.base_url}/login", json=data)

        # Then
        self.assertEqual(response.status_code, expected_status)
        self.assertIn("access_token", response.json)
        self.assertIn("refresh_token", response.json)

    @patch('app.auth_service.approve_refresh_token')
    def test_refresh_token(self, mock_approve_refresh_token):
        # Given
        mock_approve_refresh_token.return_value = {
            "access_token": "new_access_token",
            "refresh_token": "new_refresh_token"
        }
        data = {
            "refresh_token": "test_refresh_token"
        }
        expected_status = 200

        # When
        response = self.client.put(f"{self.base_url}/login", json=data)

        # Then
        self.assertEqual(response.status_code, expected_status)
        self.assertIn("access_token", response.json)
        self.assertIn("refresh_token", response.json)
        self.assertEqual(response.json["access_token"], "new_access_token")
        self.assertEqual(response.json["refresh_token"], "new_refresh_token")
