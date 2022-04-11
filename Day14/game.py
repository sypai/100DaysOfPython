from art import logo, versus
from data import data
import random

# Show Logo and Welcome
print(logo)
print("\nWelcome to this frustratingly addictive game - where you guess who has more instagram followers!")

# Game Section
# Get Comparison data
def get_data():
    return random.choice(data)

# Comparison Checker
def check(choice, followerA, followerB, curr_score):
    winner = 1 # This variable tells which obj wins. 1 for A and 2 for B

    if choice == 'A' or choice == 'a':
        if objA_followers >= objB_followers:
            curr_score += 1
        else:
            curr_score = 0
    elif choice == 'B' or choice == 'b':
        if objA_followers <= objB_followers:
            curr_score += 1
            winner = 2
        else:
            curr_score = 0
    return curr_score, winner

# Show score
score = 0
flag = True

objA = get_data()
objB = get_data()

while flag:
    print(f"\nYour score is {score}")
    
    objA_followers = objA.get('follower_count')
    objB_followers = objB.get('follower_count')

    print(f"\nCompare A: {objA.get('name')}, a {objA.get('description')}. from {objA.get('country')}.")
    print(versus)
    print(f"\nWith B: {objB.get('name')}, a {objB.get('description')}. from {objB.get('country')}.")

    choice = input("\n-------------------------------------------------------------------------\nWho has more followers? Choose 'A/a' OR 'B/b ===> ")
    curr_score, winner = check(choice, objA_followers, objB_followers, score)

    if curr_score == 0:
        flag = False
        print("Oops! That was wrong...Your final score is: ", score)
        break

    score = curr_score
    if winner == 1: 
        objB = objA
        objA = get_data()
    else:
        objA = get_data()