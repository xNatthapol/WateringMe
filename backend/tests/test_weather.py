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

    def test_weather_hour_wrong_date_format(self):
        """Ensure the weather by hour endpoint returns a successful response."""
        response = self.client.get(f"/weather/hour/{self.wrong_formatted_date}/{self.hour}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'Not Found'})

    def test_weather_hour_negative_hour(self):
        """Ensure the weather by hour endpoint returns a successful response."""
        response = self.client.get(f"/weather/hour/{self.date}/{self.negative_hour}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {
            'detail': 'Weather data not found for the specified date and hour'})

    def test_weather_hour_unreal_date(self):
        """Ensure the weather by hour endpoint returns a successful response."""
        response = self.client.get(f"/weather/hour/{self.invalid_date}/{self.hour}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Not Found"})

    def test_weather_hour_unreal_date_and_neg_hr(self):
        """Ensure the weather by hour endpoint returns a successful response."""
        response = self.client.get(f"/weather/hour/{self.invalid_date}/{self.negative_hour}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Not Found"})

    def test_weather_hour_string_hour(self):
        """Ensure the weather by hour endpoint returns a successful response."""
        response = self.client.get(f"/weather/hour/{self.date}/{self.string_hour}")
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), {'detail': [{'input': '42o',
                                                        'loc': ['path', 'hour'],
                                                        'msg':
                    'Input should be a valid integer, unable to parse string '
                    'as an integer','type': 'int_parsing'}]})

    def test_weather_day(self):
        """Ensure the weather by day endpoint returns a successful response."""
        response = self.client.get(f"/weather/day/{self.date}")
        self.assertEqual(response.status_code, 200)
