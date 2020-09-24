import requests 



#for air quality 
zip_code ='92706'
date ='2020-09-23'
api_key = ''#your API key 

r = requests.get('http://www.airnowapi.org/aq/forecast/zip_code/?format=application/json&zipCode='+zip_code+'&date='+date+'&distance=50&API_KEY='+api_key)

print(r.json())
#http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&
# zipCode=92706&date=2020-09-23&distance=25&API_KEY=


class AirQuality:

    def __init__(self):

        self.url = requests.get('/')

#parse through the data 
    def get_air_quality(self):

        data = self.url.json()
