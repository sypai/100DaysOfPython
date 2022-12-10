# List Comprehension
# new_list = [item for item in list]

# Square numbers
numbers = [1, 2, 3, 4, 5]
new_list = [n*n for n in numbers]
print(new_list)

# Capitalize names with letters more than 5
names = ['Mahendra', 'Tendulkar', 'Cristiano', 'Robert', 'Tom', 'Lionel', 'Virat', 'Ronaldo']
big_names = [name.upper() for name in names if len(name) > 6]
print(big_names)

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for key, value in dict.items() if test}

# Exercise 1
sentence = "What is the airspeed velocity of an unladen swallow"
words = sentence.split(" ")
count = {letters:len(letters) for letters in words}
print(count)

