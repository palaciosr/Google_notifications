from datetime import date, timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from httplib2 import Http
from apiclient import discovery
from Api_Notifications.covid_cases import CovidCases
from Api_Notifications.air_quality import AirQuality
from Api_Notifications.weather_forecast import WeatherForecast


class GoogleCalendar:
    """
    This class authenticates to Google calendar in order to
    post events. Here it will post events such as covid cases
    in the US, air quality, and weather forecast.

    """

    def __init__(self):
        

        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
    
        #this would be after the user allow permission to the google calendar API
        # include site  would need path where credentials got downloaded
        self.CREDENTIALS_FILE = '/Users/rodo/Downloads/credentials.json'
        self.email ='palaciosr080@gmail.com'
        self.get_covid_cases = CovidCases().get_cases()
        self.get_air_quality = AirQuality().get_air_quality()
        self.get_weather_forecast = WeatherForecast().get_weather_forecast()


    def get_calendar_service(self):
        """
        The file token.pickle stores the user's access and refresh tokens, and is
        created automatically when the authorization flow completes for the first
        time.
        """

        creds = None
        
        #  User needs to safe the path locally. 
        if os.path.exists('/Users/rodo/Downloads/token.pickle'):
            with open('/Users/rodo/Downloads/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.CREDENTIALS_FILE, self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('/Users/palac/Desktop/token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        service = build('calendar', 'v3', credentials=creds)
        return service

#needs to call APIs daily 
    def post_weather_to_calendar(self):

        TIMEZONE = 'America/Los_Angeles'
        EVENT_ID = 'primary'
        event = {
            'summary': 'COVID cases in the US today: '+ self.get_covid_cases, +' '+'the weather today is :'#will have weather,air quality , and covid cases 
            'location': 'hell',
            'start': {
            'dateTime': date.today(),#'2020-09-20T10:00:00.000-07:00', #change to dynamic
            'timeZone': 'America/Los_Angeles'
        },
            'end': {
            'dateTime': date.today() + timedelta(5),#'2020-09-21T10:25:00.000-07:00',
            'timeZone': 'America/Los_Angeles'
        },
            'recurrence':[
                'RRULE:FREQ=WEEKLY;UNTIL=20200925T170000Z'
            ],
            'attendees':[
                {
                    'email':'palaciosr080@gmail.com'
                }
            ],
        }

s=GoogleCalendar().get_calendar_service()

# recurring_event = s.events().insert(calendarId=EVENT_ID,body=event).execute()