import pandas as pd

# Creating Data Frame for CSV
data = pd.read_csv('nato_phonetic_alphabet.csv')

# Dictionary Comprehension to create dictionary like 'A': Alfa
nato_dict = {row.letter:row.code for index, row in data.iterrows()}

def generate_phonetic():
    # Take User Input
    name = input("Enter your name?\n===> ")

    try:
        nato_list = [nato_dict[letter.upper()] for letter in name]
    except KeyError:
        print('Sorry, only letters in the alphabet please')
        generate_phonetic()
    else:
        print(nato_list)

generate_phonetic()