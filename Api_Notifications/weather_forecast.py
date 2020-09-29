import requests 



#weather forecast
print("please input the zip code of your city you would ")
zip_code_city = input()
appid =''
x = 'http://api.openweathermap.org/data/2.5/weather?zip='+zip_code_city+'&units=imperial'+'&appid='+appid
r = requests.get(x)
r.status_code
result = r.json()
print(result)


class WeatherForecast:


    def __init__(self):


        self.zip_code_city = '92706'
        self.appid = ''

        self.url = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+self.zip_code_city+'&units=imperial'+'&appid='+self.appid)

    def get_weather_forecast(self):

        data = self.url.json()
