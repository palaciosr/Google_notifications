import requests

class CovidCases:

    def __init__(self):
        
        self.url = requests.get('http://corona-api.com/countries/US')

    def get_cases(self):

        data = self.url.json()
        # print(data)

        country_name = data['data']['name']
        updated_date = data['data']['updated_at']
        cases = data['data']['today']['confirmed']
        deaths = data['data']['today']['deaths']

        return country_name,updated_date,deaths,cases


c,date,deaths,cases = CovidCases().get_cases()
print(c,date,deaths,cases)