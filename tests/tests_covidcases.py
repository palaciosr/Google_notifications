import requests
import unittest

class ApiTest(unittest.TestCase):

    def test_check_api(self):


        response =requests.get('http://corona-api.com/countries/US')
        print(response.status_code)

        self.assertEqual(response.status_code,200)


ApiTest().test_check_api()