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

    def test_weather_valid_date_and_hour(self):
        """Ensure the weather by hour endpoint returns a successful response."""
        response = self.client.get(f"/weather/hour/{self.date}/{self.hour}")
        self.assertEqual(response.status_code, 200)

    def test_weather_200_response_body(self):
        """Ensure the weather by hour endpoint returns a successful response."""
        response = self.client.get(f"/weather/hour/{self.date}/{self.hour}")
        self.assertEqual(response.json(), {'condi': 'Partly cloudy',
                                           'conic': '//cdn.weatherapi.com/weather/64x64/day/116.png',
                                           'humid': 30.0,
                                           'lat': 13.84,
                                           'light': 91.0,
                                           'lon': 100.57,
                                           'precip': 0.0,
                                           'temper': 40.0,
                                           'ts': '2024-05-05T15:00:00'}
                         )

    def test_weather_hour_wrong_date_format(self):
        """Ensure the weather by hour endpoint returns a successful response."""
        response = self.client.get(
            f"/weather/hour/{self.wrong_formatted_date}/{self.hour}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {'detail': 'Not Found'})

    def test_weather_hour_negative_hour(self):
        """Ensure the weather by hour endpoint returns a successful response."""
        response = self.client.get(
            f"/weather/hour/{self.date}/{self.negative_hour}")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {
            'detail': 'Hour value cannot be negative'})

    def test_weather_hour_unreal_date(self):
        """Ensure the weather by hour endpoint returns a successful response."""
        response = self.client.get(
            f"/weather/hour/{self.invalid_date}/{self.hour}")
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), {'detail': [
            {'ctx': {'error': 'month value is outside expected range of 1-12'},
             'input': '3000-13-40',
             'loc': ['path', 'date'],
             'msg': 'Input should be a valid date or datetime, month value is '
                    'outside expected range of 1-12',
             'type': 'date_from_datetime_parsing'}]})

    def test_weather_hour_string_hour(self):
        """Ensure the weather by hour endpoint returns a successful response."""
        response = self.client.get(
            f"/weather/hour/{self.date}/{self.string_hour}")
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json(), {'detail': [{'input': '42o',
                                                       'loc': ['path', 'hour'],
                                                       'msg':
                                                           'Input should be a valid integer, unable to parse string '
                                                           'as an integer',
                                                       'type': 'int_parsing'}]})

    def test_weather_day(self):
        """Ensure the weather by day endpoint returns a successful response."""
        response = self.client.get(f"/weather/day/{self.date}")
        self.assertEqual(response.status_code, 200)
