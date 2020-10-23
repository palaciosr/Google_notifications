from datetime import date, timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from httplib2 import Http
from apiclient import discovery
from Api_Notifications.CovidCases import CovidCases
# from Api_Notifications.air_quality import AirQuality
from Api_Notifications.WeatherForecast import WeatherForecast


class GoogleCalendar:
    """
    This class authenticates to Google calendar in order to
    post events. 
    google_calendar = GoogleCalendar('palaciosr080@gmail.com')

    Post an event as a string with one or more arguments 

    post_event = google_calendar.post_to_calendar(event)

    """

    def __init__(self,recipient):
        

        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
    
        #this would be after the user allow permission to the google calendar API
        # once on site download  the json file and store it on the root folder
        self.CREDENTIALS_FILE = 'credentials.json'
        self.email = recipient

    def get_calendar_service(self):
        """
        The file token.pickle stores the user's access and refresh tokens, and is
        created automatically when the authorization flow completes for the first
        time.
        """

        creds = None
        
        #  User needs to safe the path locally. 
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
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
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        service = build('calendar', 'v3', credentials=creds)
        return service


    def event(self,*args):

        """
        This method creates an event using summary as the text
        to be specified date,time, and location.
        The recipient and if it needs to reccurent and until what date.

        For this example, in summary  we use the APIs and renders COVID cases, 
        weather forecast and air quality. 
        """

        TIMEZONE = 'America/Los_Angeles'

        event = {
            'summary': 'COVID cases'+str(cases)+ 'in the'+ str(country_name)+ 'today:' + str(updated_date)+ 'number of deaths: '+str(deaths) +'the weather today is :' +str(temperature) + 'in'+str(city_name),
            'location': 'hell',
            'start': {
            'dateTime': date.today(),
            'timeZone': TIMEZONE
        },
            'end': {
            'dateTime': date.today() + timedelta(5),
            'timeZone': TIMEZONE
        },
            'recurrence':[
                'RRULE:FREQ=WEEKLY;UNTIL=20200925T170000Z'
            ],
            'attendees':[
                {
                    'email': self.email
                }
            ],
        }

        return event

#needs to call APIs daily 
    def post_to_calendar(self,event):

        """
        This method finally checks that the Google account is authenticated
        once confirmed it sends the event to your Google calendar
        """

        EVENT_ID = 'primary'

        service=GoogleCalendar().get_calendar_service()

        if service:

            recurring_event = service.events().insert(calendarId=EVENT_ID,body=event).execute()

        else:
            print('Event is not correctly authenticated')

if __name__ == '__main__':

    google_calendar = GoogleCalendar('email')

    country_name,updated_date,cases,deaths = CovidCases().get_cases()
    # self.get_air_quality = AirQuality().get_air_quality()
    city_name,temperature = WeatherForecast().get_weather_forecast()

    event = google_calendar.event(country_name,updated_date,cases,deaths,city_name,temperature)

    #Sending to event API responses for COVID, air quality, and weather forecast.
    GoogleCalendar().post_to_calendar(event)