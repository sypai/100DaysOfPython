import random

word_list = ["aardvark", "baboon", "camel"]
size = len(word_list)

word = word_list[random.randint(0, size - 1)]

guess = input("Guess a letter ==> ")

for letter in word:
    if guess == letter:
        print("You live!")
    else:
        print("You die!")
