import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
size = len(chosen_word)

blank_list = ["__"]*size

while True:
    guess = input("Guess a letter: ").lower()

    idx = 0
    for letter in chosen_word:
        if letter == guess:
            blank_list[idx] = letter
        idx += 1

    for char in blank_list:
        print(char, end=" ")

    if "__" in blank_list:
        print("")
        continue
    break
