from unittest.mock import patch, MagicMock

from tests.base_test import BaseTestCase


class TestSoilEndpoints(BaseTestCase):
    """Test cases for soil-related endpoints."""

    def test_soil_current(self):
        """Ensure the soil current conditions endpoint returns a successful response."""
        response = self.client.get("/soil/current")
        self.assertEqual(response.status_code, 200)

    def test_soil_forecast(self):
        """Ensure the soil forecast endpoint returns a successful response."""
        response = self.client.get("/soil/forecast")
        self.assertEqual(response.status_code, 200)

    def test_soil_hour(self):
        """Ensure the soil conditions by specific hour endpoint returns a successful response."""
        response = self.client.get(f"/soil/hour/{self.date}/{self.hour}")
        self.assertEqual(response.status_code, 200)

    def test_soil_hour_wrong_date_format(self):
        """Ensure the soil conditions by specific hour endpoint returns a successful response."""
        response = self.client.get(f"/soil/hour/{self.wrong_formatted_date}/{self.hour}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Not Found"})

    def test_soil_hour_unreal_date(self):
        """Ensure the soil conditions by specific hour endpoint returns a successful response."""
        response = self.client.get(f"/soil/hour/{self.invalid_date}/{self.hour}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Not Found"})


    def test_soil_hour_negative_hour(self):
        """Ensure the soil conditions by specific hour endpoint returns a successful response."""
        response = self.client.get(f"/soil/hour/{self.date}/{self.negative_hour}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'Soil data not found at specified date and hour'})

    def test_soil_day(self):
        """Ensure the soil conditions by specific day endpoint returns a successful response."""
        response = self.client.get(f"/soil/day/{self.date}")
        self.assertEqual(response.status_code, 200)
