import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
computer_choice_index = random.randint(0, 2)
computer_choice = options[computer_choice_index]

print("\n=====================================================================\n"
      "Let's play Rock 🥌, Paper 📜 and Scissor ✂!")

player_choice = int(input("\nType '1' for Rock, '2' for Paper, '3' for Scissor ==> "))

print(f"\n\t\tYou Choose \n\t\t{options[player_choice - 1]}")

print(f"\n\t\tComputer Chose \n\t\t{options[computer_choice_index]}")

result = ""
if computer_choice_index == 0:  # Rock
    if player_choice == 1:  # Rock
        result = "Meh! Nobody wins"
    elif player_choice == 2:  # Paper
        result = "Woohoo! You win!"
    elif player_choice == 3:  # Scissor
        result = "You lose! Your scissor just got destroyed by THE ROCK"
    else:
        raise Exception("CHOOSE ONLY FROM 123")

elif computer_choice_index == 1:  # Paper
    if player_choice == 2:  # Rock
        result = "Meh! Nobody wins"
    elif player_choice == 3:  # Scissor
        result = "Woohoo! You win!"
    elif player_choice == 1:  # Rock
        result = "You lose! Your rock got dusted by my Paper!"
    else:
        raise Exception("CHOOSE ONLY FROM 123")

else:  # Scissor
    if player_choice == 3:  # Scissor
        result = "Meh! Nobody wins"
    elif player_choice == 1:  # Rock
        result = "Woohoo! You win!"
    elif player_choice == 2:  # Paper
        result = "You lose! I tore your paper into pieces"
    else:
        raise Exception("CHOOSE ONLY FROM 123")

print("****************************************************************************\n\t\t\t\t\t"
      "\t" +
      result +
      "\n****************************************************************************")
