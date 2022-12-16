from tkinter import *
from tkinter import messagebox
import pandas
import random
import json

# Constants
sy_font='Crimson Text'
size_font=12
WHITE = '#EEEEEE'
BLUE = '#222831'
virgin = None

# -------------------------------------------------------------------------Password Generator-------------------------------------


# website, username, password
# -------------------------------------------------------------------------Save Password------------------------------------------
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    character_set = [letters, numbers, symbols]  # Set Index

    # letters_count = random.randint(2, 5)
    # symbols_count = random.randint(2, 5)
    # numbers_count = random.randint(2, 5)
    letters_count = 5
    symbols_count = 5
    numbers_count = 5

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

        password += character_set[set_index][set_type_index]
    e3.delete(0, END)
    e3.insert(END, string=password)

def update_password():
    pass

def save_password():
    website = e1.get()
    username = e2.get()
    password = e3.get()
    # Ask User, to check input data and confirm if data is to 
    # be saved
    confirm = messagebox.askokcancel(
        title=website,
        message=f'Here are the details entered:\n\nUsername/Email: {username}\n\nPassword: {password}\n\nAre you sure?'
    )
    if confirm:
        data = {
            'website': [website],
            'username': [username],
            'password': [password]
        }
        
        messagebox.showinfo(title='sylock: Password Manager', message="Beep. Boop. Beep. Your Password has been saved successfully.")
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)

def check_password():
    website = e1.get()
    username = e2.get()
    password = e3.get()
    
    try:
        with open('data.json') as open_file:
            data = json.load(open_file)
            save_password(website, username, password, empty_file=True)
    
    except:
        global virgin
        virgin = True
        save_password(website, username, password, empty_file=True)
        
    else:
        website_list = data['website'].to_list()
        if website in website_list: 
            # If Current 'Website' is in DB,
            # check if the username is same, if it is
            # ask user if they want to update, if yes, go ahead. 
            # check = data[data.website == website].username == username
            # if check
            # if data[data.website == website].username == username:
            #     # update_password(website, username, password)
            #     print('Do you want to update the password?')
            pass
            

# -------------------------------------------------------------------------UI SETUP-----------------------------------------------

# Window
window = Tk()
window.title("sylock : World's most trusted Password Manager")
window.config(padx=150, pady=150, bg=WHITE)

# ----------- Canvas ------------
canvas = Canvas(width=220, height=220, bg=WHITE, highlightthickness=0)

img = PhotoImage(file='lock.png')
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)


############ Row 1
# 'Website' Label - l1
l1 =  Label()
l1.config(text='Website: ', font=(sy_font, size_font, 'bold'), bg=WHITE, highlightthickness=0)
l1.grid(row=1, column=0)

# 'Website' Entry - e1
e1 = Entry()
e1.config(width=55)
e1.focus()
e1.grid(row=1, column=1, columnspan=2)

filler1 = Label()
filler1.config(bg=WHITE)
filler1.grid(row=2, column=0, columnspan=3)

############ Row 2
# 'Email/Username' Label - l2
l2 = Label()
l2.config(text='Email/Username: ', font=(sy_font, size_font, 'bold'),bg=WHITE, highlightthickness=0)
l2.grid(row=3, column=0)

# 'Email/Username' Entry - e2
e2 = Entry()
e2.config(width=55)
e2.grid(row=3, column=1, columnspan=2)


filler2 = Label()
filler2.config(bg=WHITE)
filler2.grid(row=4, column=0, columnspan=3)

############ Row 3
# 'Password' Label - l3
l3 = Label()
l3.config(text='Password: ', font=(sy_font, size_font, 'bold'), bg=WHITE, highlightthickness=0)
l3.grid(row=5, column=0)

# 'Password' Entry - e3
e3 = Entry()
e3.config(width=34)
e3.grid(row=5, column=1)

# 'Generate Password' Button - b3
b3 = Button()
b3.config(text='Generate Password', bg=BLUE, fg=WHITE, bd='5', command=generate_password)
b3.grid(row=5, column=2)

filler3 = Label()
filler3.config(bg=WHITE)
filler3.grid(row=6, column=0, columnspan=3)

############# Row 4
# 'Add Password' Button - b4
b3 = Button()
b3.config(width=49, text='Add Password', bg=BLUE, fg=WHITE, bd='5', command=check_password)
b3.grid(row=7, column=1, columnspan=2)

window.mainloop()