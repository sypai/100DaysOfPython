# Importing CSV Data from file
import csv #LOL

with open('weather_data.csv') as file:
    data = csv.reader(file)
    temp_on_days = {}
    i = 0
    for row in data:
        if i == 0:
            i += 1
            continue
        temp_on_days[row[0]] = int(row[1])
    print(temp_on_days)

 