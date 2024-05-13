import unittest

from fastapi.testclient import TestClient

from app.main import app


class BaseTestCase(unittest.TestCase):
    """Base test setup for all endpoint tests."""

    def setUp(self):
        self.client = TestClient(app)
        self.date = "2024-05-05"
        self.wrong_formatted_date = "2024/05/05"
        self.invalid_date = "3000-13-40"
        self.negative_hour = "-12"
        self.string_hour = "42o"
        self.hour = "15"
