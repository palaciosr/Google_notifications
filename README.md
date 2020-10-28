# Google_notifications
Will provide air quality, weather forecast, and covid cases from current location and send them to the google calendar daily.


# Prerequisites
Will need to have a gmail account for Google calendar to work. Then will need to go to: https://developers.google.com/calendar/quickstart/python , and enable the Google calendar API, which will give you the keys to authenticate. Save those keys to the root of Google_notifications path, this is needed for google_auth.py, to authenticate.On google_auth.py line 143: email should be replace by your google email. Once this is ran the first time the terminal will take the user to their email login they have to login and give quickstart access.

Weather API to request an API key go to https://openweathermap.org/api

Air quality API to request an API key go to https://docs.airnowapi.org/account/request/

For simplicity the user will need to input each individual API key statically to config_air_quality.py and config_weather_forecast.py found in the Api_Notifications folder. The Google email will need to be inputted into google_auth.py as well
