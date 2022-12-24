import os
import requests
import datetime
from twilio.rest import Client

now = datetime.datetime.now()

###### Weather API
API_endpoint = 'https://api.weatherapi.com/v1/forecast.json'
API_KEY = os.environ.get('WEATHERAPI_KEY')
parameters =  {
    'q': '21.77,81.96',
    'key': API_KEY,
    'days': 1
}

response = requests.get(API_endpoint, params=parameters)
response.raise_for_status()

####### Weather Data
weather_data = response.json()
forecast_data = weather_data['forecast']['forecastday'][0]

# Date
months = {
    '1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June',
    '7': 'July', '8': 'August', '9': 'September', '10': 'October', '11': 'November', '12': 'December'
}
days = {
    '1': 'Monday', '2': 'Tuesday', '3': 'Wednesday', '4': 'Thursday',
    '5': 'Friday', '6': 'Saturday', '7': 'Sunday'
}
date = forecast_data['date'].split('-')
today = str(now.weekday()+1)
day = days[today]

formatted_date = f"{date[2]} {months[date[1]]}, {date[0]}. It's {day}."


# Day's Overview
condition = forecast_data['day']['condition']['text']
max_temp = forecast_data['day']['maxtemp_c']
min_temp = forecast_data['day']['mintemp_c']

# Rain Conditions
chance_of_rain = forecast_data['day']['daily_chance_of_rain']
rain_string = 'No chances of rain throughout the day.'
if chance_of_rain > 0:
    will_it_rain = forecast_data['day']['daily_will_it_rain']
    if will_it_rain == 1:
        rain_string = 'It is going to rain today. Take an umbrella with you while stepping out.'
    else:
        rain_string = 'There are slight chances of rain today.'

# Astrology 
sunrise = forecast_data['astro']['sunrise']
sunset = forecast_data['astro']['sunset']
moon_phase = forecast_data['astro']['moon_phase']

weather_string = f"""\n
Good Afternoon, Suyash.
Today is {formatted_date}
Sun rose at {sunrise}. The day is going to be {condition}, {rain_string} 
The temperatures will range from {min_temp} \N{DEGREE SIGN}C to {max_temp} \N{DEGREE SIGN}C.
Sun will set at {sunset}. It is going to be a {moon_phase} Moon tonight.
Seize the day. Be Grateful. 
"""

# # Twilio 
account_sid = 'AC97fae3612a7a0078927848da8b38d146'
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body='weather_string',
                     from_='+14094032415',
                     to='+917772800787'
                 )

print(message.status)
