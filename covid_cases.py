import requests



# r = requests.get(' https://corona-api.com/timeline')

r= requests.get(' http://corona-api.com/countries/US')
print(r.json())


class CovidCases:

    def __init__(self):
        
        self.url = requests.get('http://corona-api.com/countries/US')

    def get_cases(self):

        data = self.url.json()

        country_name = data['data']['name']

        updated_date = data['data']['updated_at']