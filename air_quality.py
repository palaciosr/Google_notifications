import requests 



#for air quality 

class AirQuality:

    def __init__(self):

        self.url = requests('/')

#parse through the data 
    def get_air_quality(self):

        data = self.url.json()
