import unittest

from fastapi.testclient import TestClient

from app.main import app


class BaseTestCase(unittest.TestCase):
    """Base test setup for all endpoint tests."""

    def setUp(self):
        self.client = TestClient(app)
        self.date = "2024-05-05"
        self.hour = "15"
