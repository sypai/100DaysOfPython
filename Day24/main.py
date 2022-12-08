input_letter_path = './Input/Letters/starting_letter.txt'

input_names_path = './Input/Names/invited_names.txt'

# Reading names and Making an array
# Using readline
names = []
with open(input_names_path) as file:
    for name in file.readlines():
        names.append(name.strip())

# Reading Starting Letter and Replacing [name] with name
with open(input_letter_path) as file:
    txt = file.read()
    
for name in names:
    with open(f'./Output/ReadyToSend/{name}.txt', 'w') as file:
        file.write(txt.replace('[name]', name))
    