import requests


response = requests.get('')

assert response.status_code == 200