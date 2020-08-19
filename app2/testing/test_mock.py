from unittest.mock import patch
from flask import url_for
from flask_testing import TestCase

from app1.app import app

class TestBase(TestCase):
    def create_app(self):
        return app
