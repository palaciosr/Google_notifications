import requests 
from datetime import date,timedelta
import json 
from config_air_quality import API_KEY

#for air quality 
zip_code ='92706'
date ='2020-09-23'
api_key =API_KEY#your API key n

#need to check that this works and returns json back

r = requests.get('http://www.airnowapi.org/aq/forecast/zip_code/?format=application/json&zipCode='+zip_code+'&date='+date+'&distance=50&API_KEY='+api_key)

print(r.status_code)
print()

print(r.json())

# data['data']['name']

# print(data['data']['name'])


#http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&
# zipCode=92706&date=2020-09-23&distance=25&API_KEY=


# class AirQuality:

#     pass 

#     def __init__(self):

#         self.zip_code = '92706'

#         #your api key 
#         self.api_key = ''

#         #today's date
#         self.date = date.today() + timedelta(1)

#         self.url = requests.get('http://www.airnowapi.org/aq/forecast/zip_code/?format=application/json&zipCode='+self.zip_code+'&date='+self.date+'&distance=50&API_KEY='+self.api_key)

# #parse through the data 
#     def get_air_quality(self):

#         data = self.url.json()
