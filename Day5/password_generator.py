import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
character_set = [letters, numbers, symbols]  # Set Index

print("=+=+==+=+==+=+==+=+==+=+==+=+==+=+=+=+=+==+=+\n\nWelcome to sypai's password generator\n")

letters_count = int(input("How many letters would you like in your password? "))
symbols_count = int(input(f"How many symbols would you like? "))
numbers_count = int(input(f"How many numbers would you like? "))

password_length = letters_count + numbers_count + symbols_count
password = ""

current_letter_count = 0
current_number_count = 0
current_symbol_count = 0

for _ in range(password_length):
    set_index = random.randint(0, 2)

    if set_index == 0:  # Letters
        if current_letter_count >= letters_count:
            set_index = random.randint(1, 2)

    if set_index == 1:  # Numbers
        if current_number_count >= numbers_count:
            if current_letter_count >= letters_count:
                set_index = 2
            else:
                temp = [0, 2]
                set_index = temp[random.randint(0, 1)]

    if set_index == 2:  # Symbols
        if current_symbol_count >= symbols_count:
            if current_letter_count >= letters_count:
                set_index = 1
            else:
                if current_number_count >= numbers_count:
                    set_index = 0
                else:
                    temp = [0, 1]
                    set_index = temp[random.randint(0, 1)]

    if set_index == 0:
        current_letter_count += 1
        set_type_index = random.randint(0, 51)
    elif set_index == 1:
        current_number_count += 1
        set_type_index = random.randint(0, 9)
    elif set_index == 2:
        current_symbol_count += 1
        set_type_index = random.randint(0, 8)

    # print(set_index, set_type_index)
    password += character_set[set_index][set_type_index]

print("==============================================================\n")
print(f"Your highly secure password =>  \t\t{password}\n")
print("==============================================================\n")

print(f"{current_letter_count} Letters, {current_symbol_count} symbols"
      f" and {current_number_count} numbers")

