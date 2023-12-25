import requests

API_KEY = '422a8f7f597508bec39bb048447046cc'
LATTITUDE = 42.443962
LONGITUDE = -76.501884
#1ZZQJQNYXPEKV4QGX9YUHT2S

url = 'https://api.openweathermap.org/data/2.5/forecast'
params = {
    'lat' : LATTITUDE,
    'lon' : LONGITUDE,
    'appid' : API_KEY,
    'cnt' : 4
}

response = requests.get(url, params = params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data['list']:
    weather_id = hour_data['weather'][0]['id']

    if int(weather_id) < 700:
        will_rain = True

if will_rain:
    print('Bring an umbrella!') 