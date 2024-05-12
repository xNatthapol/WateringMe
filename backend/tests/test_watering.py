from tests.base_test import BaseTestCase


class TestWateringEndpoints(BaseTestCase):
    """Test cases for watering endpoint."""

    def test_watering_endpoint(self):
        """Ensure the watering endpoint returns a successful response."""
        soil_type = "Loam"
        response = self.client.get(f"/watering?soil_type={soil_type}")
        self.assertEqual(response.status_code, 200)
