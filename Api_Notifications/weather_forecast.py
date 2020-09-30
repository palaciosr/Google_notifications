import requests 


class WeatherForecast:


    def __init__(self):


        self.zip_code_city = '92706'
        self.appid = ''

        self.url = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+self.zip_code_city+'&units=imperial'+'&appid='+self.appid)

    def get_weather_forecast(self):

        data = self.url.json()

        city_name = data['name']
        temperature = data['main']['temp']

        return city_name,temperature
