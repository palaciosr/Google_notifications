import requests




response =requests.get('http://corona-api.com/countries/US')


assert(response.status_code) == 200