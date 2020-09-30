# Google_notifications
Will provide air quality, weather forecast, and covid cases from current location and send them to the google calendar daily.


# Prerequisites
Will need to have a gmail account for Google calendar to work. Then will need to go to: https://developers.google.com/calendar/quickstart/python , and enable the Google calendar API, which will give you the keys to authenticate. Save those keys to a path, save that path as it would be need on google_auth.py, to authenticate. 

Weather API to request an API key go to https://openweathermap.org/api

Air quality API to request an API key go to https://docs.airnowapi.org/account/request/

For simplicity the user will need to input each individual API key statically to air_quality.py and weather_forecast.py found in the Api_Notifications folder. The Google email will need to be inputted into google_auth.py 
