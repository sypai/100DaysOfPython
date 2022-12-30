import requests
import datetime

# Get today's date
now = datetime.datetime.now()
today = now.strftime("%-d/%m/%Y")
time = now.strftime("%X")

# Nutritionix API 
nutritionix_ID = ''
nutritionix_KEY = ''

nutritionix_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': nutritionix_ID,
    'x-app-key': nutritionix_KEY,
    'x-remote-user-id': '0',
    'Content-Type': 'application/json'
}

# Take Input
activity_input = input("What activity would you like to add?\n")

parameters = {
    'query': activity_input,
    'gender': 'male',
    'weight_kg': 65,
    'height_cm': 173,
    'age': 25
}

response = requests.post(url=nutritionix_endpoint, json=parameters, headers=headers)

data = response.json()

record = {
    'workout' : 
        {
        'date' : today,
        'time' : time,
        'exercise' : data['exercises'][0]['name'].title(),
        'duration' : data['exercises'][0]['duration_min'],
        'calories' : data['exercises'][0]['nf_calories'],
        }
    
}

# Sheety API setup
sheety_endpoint = 'https://api.sheety.co/6a7ead403ffe79d80b95b93b9d4b8087/day38MyWorkouts/workouts'

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url=sheety_endpoint, json=record, headers=headers)
# response = requests.delete(sheety_endpoint)
print(record)
print(response.text)