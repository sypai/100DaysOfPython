""" Guessing game
Program selects a random number and then the user has to guess it. User selects the difficulty (Easy/Hard)
which sets the number of attempts they get to guess the number
If the guess is right, hurrah but if the guess is wrong, the program hints by telling if the guess is 
higher or lower than the number 
"""

# Choose a number
import random
num = random.randint(0, 500)

# Welcome User
print("Welcome to this Guessing Game - Higher or Lower")
print("The number is between 0 & 500")

# Select Difficulty
difficulty = int(input("\nSelect Difficulty for the game: \n 1. Easy (10 attempts)\n 2. Hard (3 attempts)\n===> "))
if difficulty == 1:
    choice = 10
elif difficulty == 2:
    choice = 3

print("Let's begin!\n \n")

# Ask for guesses
while choice > 0:
    guess = int(input("What is your guess?\n===> "))
    if guess == num:
        print("Yes! That's the number")
        break
    else: 
        print("That's a wrong guess!")
        if guess > num: 
            print("That's high! Number is smaller than this.")
        else:
            print("That's lower! Number is bigger than this.") 
        choice -= 1 
    
    print(f"\n{choice} attempts left.\n")
    if choice == 0:
        print("Oops! You couldn't guess the number. No attempts left. Play again!")