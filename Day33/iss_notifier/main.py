import requests
from datetime import datetime as dt
from time import sleep
import math
import smtplib 

# Constants
MY_LAT = 13.038031
MY_LONG = 77.617104
MY_EMAIL = 'suyashbajpai.web@gmail.com'
MY_PASSWORD = 'qoxvlsvsbdtpliau'
address = 'smtp.gmail.com'
    
def is_overhead(): 
    # ISS Location API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])
    print(f'{iss_latitude}, {iss_longitude}')
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True 

def utc_to_ist(time):
    # Take Hours, Minutes, Seconds and add 5 hours, 30 mins to it.
    time_to_secs = time[0]*3600 + time[1]*60 + time[2]
    ist_in_secs = time_to_secs + 19800
   
    ist = [0, 0, 0]
   
    ist[0] = math.floor(ist_in_secs / 3600)
    rem_secs = ist_in_secs % 3600
   
    ist[1] = math.floor(rem_secs / 60)
    rem_secs %= 60
   
    ist[2] = rem_secs

    return ist

def is_night():
    now = dt.now()
    # Sunrise Sunset API
    parameters = {
        'lat':MY_LAT,
        'lng':MY_LONG,
        'formatted': 0
    }

    sunrise_sunset_api = 'https://api.sunrise-sunset.org/json'

    response = requests.get(sunrise_sunset_api, params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data['results']['sunrise'].split('T')[1].split('+')[0].split(':')
    sunset = data['results']['sunset'].split('T')[1].split('+')[0].split(':')

    sunrise_ist = [int(n) for n in sunrise]
    sunset_ist = [int(n) for n in sunset]

    # Check if it is night
    if now.hour >= utc_to_ist(sunset_ist)[0] or now.hour <= utc_to_ist(sunrise_ist)[0]:
        return True
    
def notify():
    MSG = f'Subject:ISS is just crossing you by!\n\nHey, Suyash. \nStep out! ISS is over your place!\nWoohoo!'
    with smtplib.SMTP(address) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs='suyashbajpai.dev@gmail.com',
            message=MSG
        )

while True:
    sleep(60)
    if is_overhead() and is_night():
        notify()


