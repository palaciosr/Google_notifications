import requests
import unittest
from Api_Notifications.config_weather_forecast import API_KEY


class TestWeatherForecast(unittest.TestCase):

    #will pass this test if the API key is not empty
    def test_api_key(self):

        
        self.assertTrue(API_KEY)

    def test_api(self):

        url = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=92706&units=imperial'+'&appid='+API_KEY)

        self.assertEqual(url.status_code,200)
