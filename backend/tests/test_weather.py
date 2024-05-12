from tests.base_test import BaseTestCase


class TestWeatherEndpoints(BaseTestCase):
    """Test cases for weather-related endpoints."""

    def test_weather_current(self):
        """Ensure the current weather endpoint returns a successful response."""
        response = self.client.get("/weather/current")
        self.assertEqual(response.status_code, 200)

    def test_weather_forecast(self):
        """Ensure the weather forecast endpoint returns a successful response."""
        response = self.client.get("/weather/forecast")
        self.assertEqual(response.status_code, 200)

    def test_weather_hour(self):
        """Ensure the weather by hour endpoint returns a successful response."""
        response = self.client.get(f"/weather/hour/{self.date}/{self.hour}")
        self.assertEqual(response.status_code, 200)

    def test_weather_day(self):
        """Ensure the weather by day endpoint returns a successful response."""
        response = self.client.get(f"/weather/day/{self.date}")
        self.assertEqual(response.status_code, 200)
