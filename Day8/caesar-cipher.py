from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
print('+++===========+++===========+++===========+++===========+++\n')


def caesar_cipher(flow, text_input, shift_amount):
    new_text = ""
    for letter in text_input:
        if letter == ' ':
            new_text += ' '
            continue
        curr_position = alphabet.index(letter)
        if flow == 'encode':
            new_position = curr_position + shift_amount
            if new_position > 26:
                new_position -= 26
        elif flow == 'decode':
            new_position = curr_position - shift_amount
            if new_position < 0:
                new_position += 26
        new_text += alphabet[new_position]
    print(f'The {flow}d text is {new_text}')


should_end = False
while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26

    caesar_cipher(text_input=text, shift_amount=shift, flow=direction)

    print('+++===========+++===========+++===========+++===========+++\n')
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
