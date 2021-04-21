import random

names = input("Enter the names of all the people p(l)aying!\n")

players = names.split(', ')

payer = players[(random.randint(0, len(players) - 1))]

print(f"{payer} is going to buy the meal today!")
