import random

end_of_game = False
lives = 6

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
size = len(chosen_word)

blank_list = ["__"]*size

print("Welcome to the most popular game of all time!\n THE HANGMAN!")

# print(f"\n\t{stages[-1]}")
while True:
    guess = input("\nGuess a letter: ").lower()

    idx = 0
    flag = False
    for letter in chosen_word:
        if letter == guess:
            blank_list[idx] = letter
            flag = True
        idx += 1

    if not flag:
        lives -= 1
        # print(stages[lives])

    if lives == 0:
        print(f'Sentenced to death! You lose! \nThe word was | {chosen_word} |')
        break

    for char in blank_list:
        print(char, end=" ")

    if "__" in blank_list and lives > 0:
        print("")
        continue
    break

