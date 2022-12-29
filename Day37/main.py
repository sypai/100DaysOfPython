import requests
from datetime import datetime
import json

# Constants
with open('data.json', 'r') as data_file:
    data = json.load(data_file)

    USERNAME = data['credentials']["USERNAME"]
    TOKEN = data['credentials']["TOKEN"]

# Pixela API endpoint
pixela_api_endpoint = 'https://pixe.la/v1/users'

parameters = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

### This is run only once, and our account is created
# response = requests.post(url=pixela_api_endpoint, json=parameters)
# print(response.text)

# Pixela Graph Endpoint
graph_endpoint = f'{pixela_api_endpoint}/{USERNAME}/graphs'

graph_config = {
    'id' : 'graph1',
    'name' : 'I did not!',
    'unit': 'sypai-coins',
    'type': 'int',
    'color': 'kuro',
}

headers = {
    'X-USER-TOKEN' : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

#### Adding a pixel to the Habit Tracker 
adding_pixel_endpoint = f'{graph_endpoint}/graph1'

today = datetime.now()
pixel_data = {
    'date' : today.strftime("%Y%m%d"),
    'quantity' : '9'
}

# response = requests.post(url=adding_pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

### Updating a previous data
date = '20221212'
updating_data_endpoint = f'{adding_pixel_endpoint}/{date}'

updated_data = {
    'quantity': '24'
}
response = requests.put(url=updating_data_endpoint, json=updated_data, headers=headers)
print(response.text)