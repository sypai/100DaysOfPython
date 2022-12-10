import pandas as pd

# Creating Data Frame for CSV
data = pd.read_csv('nato_phonetic_alphabet.csv')

# Dictionary Comprehension to create dictionary like 'A': Alfa
nato_dict = {row.letter:row.code for index, row in data.iterrows()}

# Take User Input
name = input("Enter your name?\n===> ")
nato_list = [nato_dict[letter.upper()] for letter in name]
print(nato_list)