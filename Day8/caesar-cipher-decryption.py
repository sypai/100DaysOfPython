alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def decrypt(encrypted_text, shift_amount):
    plain_text = ""
    for letter in encrypted_text:
        curr_position = alphabet.index(letter)
        new_position = curr_position - shift_amount
        if new_position < 0:
            new_position += 26
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")


decrypt('ezqz', 5)