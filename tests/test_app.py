# tests/test_app.py
import unittest
from app import app

class TestApp(unittest.TestCase):
    def test_hello(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Hello, CI/CD World!")
