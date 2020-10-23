import requests 
from datetime import date,timedelta
import json 
from config_air_quality import API_KEY

class AirQuality:

    def __init__(self):

        self.zip_code = '92618'
        self.api_key = API_KEY
        self.date = str(date.today()-timedelta(1))
        self.url  = requests.get('http://www.airnowapi.org/aq/forecast/zipcode/?format=application/json&zipCode='+self.zip_code+'&date='+self.date+'&distance=50&API_KEY='+self.api_key)

    def get_air_quality(self):

        data = self.url.json()
        air_quality = data[0]['AQI']

        return air_quality
