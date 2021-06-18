alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount):
    encrypted_text = ''
    for letter in plain_text:
        curr_position = alphabet.index(letter)
        new_position = curr_position + shift_amount
        if new_position > 26:
            new_position -= 26
        encrypted_text += alphabet[new_position]
    return encrypted_text


print(encrypt('zulu', 5))