from tests.base_test import BaseTestCase


class TestPetEndpoints(BaseTestCase):
    """Test cases for pet forecast endpoint."""

    def test_pet_forecast(self):
        """Ensure the pet forecast endpoint returns a successful response."""
        response = self.client.get("/pet/forecast")
        self.assertEqual(response.status_code, 200)
