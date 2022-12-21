import requests
import datetime

data = datetime.datetime.now()
now = []
now.append(data.hour)
now.append(data.minute)
now.append(data.second)

sunrise_sunset_api = 'https://api.sunrise-sunset.org/json'

# King's PG 
lat0 = 13.038031
lng0 = 77.617104

parameters = {
    'lat':lat0,
    'lng':lng0,
    'formatted': 0
}

response = requests.get(sunrise_sunset_api, params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data['results']['sunrise'].split('T')[1].split('+')[0].split(':')
sunset = data['results']['sunset'].split('T')[1].split('+')[0].split(':')

for i in range(3):
    print(sunrise[i], now[i], sunset[i])
    