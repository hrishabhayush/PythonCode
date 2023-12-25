import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

API_KEY = 'your api key'
LATTITUDE = 42.443962
LONGITUDE = -76.501884
URL = 'https://api.openweathermap.org/data/2.5/forecast'

#1ZZQJQNYXPEKV4QGX9YUHT2S
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']


params = {
    'lat' : LATTITUDE,
    'lon' : LONGITUDE,
    'appid' : API_KEY,
    'cnt' : 4
}

response = requests.get(URL, params = params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data['list']:
    weather_id = hour_data['weather'][0]['id']

    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an umbrella.",
                        from_='Trial number from Twilio',
                        to='Your verified number'
                    )
#The number generated from Twilio goes under from and your number goes to to. 
