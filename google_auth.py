import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from httplib2 import Http
from apiclient import discovery

SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS_FILE = '/Users/rodo/Downloads/credentials.json'
def get_calendar_service():
   creds = None
   # The file token.pickle stores the user's access and refresh tokens, and is
   # created automatically when the authorization flow completes for the first
   # time.
   if os.path.exists('token.pickle'):
       with open('token.pickle', 'rb') as token:
           creds = pickle.load(token)
   # If there are no (valid) credentials available, let the user log in.
   if not creds or not creds.valid:
       if creds and creds.expired and creds.refresh_token:
           creds.refresh(Request())
       else:
           flow = InstalledAppFlow.from_client_secrets_file(
               CREDENTIALS_FILE, SCOPES)
           creds = flow.run_local_server(port=0)
       # Save the credentials for the next run
       with open('token.pickle', 'wb') as token:
           pickle.dump(creds, token)
   service = build('calendar', 'v3', credentials=creds)
   return service
s = get_calendar_service()


# TIMEZONE = 'America/Los_Angeles'
# EVENT_ID = 'primary'
# event = {
#     'summary': 'Appointment with people',
#     'location': 'hell',
#     'start': {
#     'dateTime': '2020-09-20T10:00:00.000-07:00', #change to dynamic
#     'timeZone': 'America/Los_Angeles'
# },
#     'end': {
#     'dateTime': '2020-09-21T10:25:00.000-07:00',
#     'timeZone': 'America/Los_Angeles'
# },
#     'recurrence':[
#         'RRULE:FREQ=WEEKLY;UNTIL=20200925T170000Z'
#     ],
#     'attendees':[
#         {
#             'email':'palaciosr080@gmail.com'
#         }
#     ],
# }
# recurring_event = s.events().insert(calendarId=EVENT_ID,body=event).execute()