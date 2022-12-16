import pandas

# Reading csv file using pandas
data = pandas.read_csv('weather_data.csv')

# print(data)

# ### Getting average temperature

# # Method 1
# temp_list = data["temp"].to_list()
# avg = sum(temp_list)/len(temp_list)
# print(avg)

# # Method 2
# print(data['temp'].mean())

# ### Get Maximum Temp

# # Using pandas series' method
# print(data['temp'].max())

# ### Selecting a column
# data['temp']
# data.temp

# ### Selecting a row
# print(data[data.day == 'Monday'])

# ## Get the row where temp is maximum
# print(data[data.temp == data.temp.max()])

## Get Monday's temperature in Fahrenheit
monday = data[data.day == 'Monday']
print(monday.temp)

# Creating a data frame from Scratch
# my_dict = {
#     'Name': ['Rohit', 'Suyash', 'Utkarsh'],
#     'Age':[24, 25, 22],
#     'Status': ['Relationship', 'Single', 'Single'] 
# }

# frame = pandas.DataFrame(my_dict)
# frame.to_csv('age.csv')