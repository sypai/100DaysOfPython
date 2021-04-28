import random
from hangman_words import word_list
from hangman_art import stages, logo

end_of_game = False
lives = 6

chosen_word = random.choice(word_list)
size = len(chosen_word)

blank_list = ["__"]*size

print(logo)

print("GAME RULES:"
      "\n:: Computer chooses a word from the english dictionary"
      "\n:: You will see how long the word is"
      "\n:: Start guessing what the word is one letter at a time."
      "\n:: The game begins with a hanging rope, each wrong guess hangs a part of our man"
      "\n:: Make your guesses right else the man hangs!")

print(f"\n\t{stages[-1]}")

for char in blank_list:
    print(char, end=" ")
print("")

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
        print(stages[lives])

    if lives == 0:
        print(f'Sentenced to death! You lose! \nThe word was | {chosen_word} |')
        break

    for char in blank_list:
        print(char, end=" ")

    if "__" in blank_list and lives > 0:
        print("")
        continue
    break

