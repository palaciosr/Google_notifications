import requests
from Api_Notifications.config_weather_forecast import API_KEY

url = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=92706&units=imperial'+'&appid='+API_KEY)


assert url.status_code == 200