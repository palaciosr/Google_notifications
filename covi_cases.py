import requests



# r = requests.get(' https://corona-api.com/timeline')

r= requests.get(' http://corona-api.com/countries/US')


print(r.json())