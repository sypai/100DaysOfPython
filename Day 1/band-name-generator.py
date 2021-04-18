# This program will suggest a band name by combining the name of the city you grew up in
# and the name of your pet

# Greet the user
print("Hello, The quest for your band name ends here!")

# Ask the user for the city they grew up in
city_name = input("Which city did you grew up in?\n")

# Ask the user for the name of a pet
pet_name = input("What is your favorite pet name?\n")

# Combine the name of their city and pet and show them their band name
band_name = city_name + " " + pet_name
print("You would be called " + band_name + ", Everybody would love this!")
