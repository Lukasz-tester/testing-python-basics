# 'super' class for tests, lets change global settings for testing

from unittest import TestCase
from app import app

class BaseTest(TestCase):
    def setUp(self):
        app.testing = True  # tells flask that for the lifetime of this app we are in testing mode
        # testing mode = exceptions and errors surface in a different way than when running the app normally
        self.app = app.test_client
