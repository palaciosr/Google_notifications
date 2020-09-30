import requests

#insert API key

url = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zip_code_city+'&units=imperial'+'&appid='+appid)


assert url.status_code == 200