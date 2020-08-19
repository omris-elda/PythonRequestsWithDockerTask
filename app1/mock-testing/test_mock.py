from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):

    def test_apes(self):
        with patch("requests.get") as g:
            g.return_value.text = "Apes"

            response = self.client.get(url_for("generate"))
            self.assertIn(b"Gibber", response.data)