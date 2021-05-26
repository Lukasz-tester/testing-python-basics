from unittest import TestCase
from app import app
import json

class TestHome(TestCase):

    def test_home(self):
        # we initialise the context manager (the block starting with "with" below)
        with app.test_client() as c:  # initialise test_client and call it "c"
            # test_client let's us make request without running full app
            resp = c.get('/')
            # resp gets the value of whatever is returned by a get request at the "/" endpoint made by client c 

            self.assertEqual(resp.status_code, 200)
            # check if the request status code is 200 (default)

            self.assertEqual(
            # compare the data returned by app with the expected dictionary
                json.loads(resp.get_data()),  #loads = load string >.> turn into json representation (a dict in Python)
                {'message': 'Hello world'}
            )
