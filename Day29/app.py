from tkinter import *
from tkinter import messagebox
import pandas

# Constants
sy_font='Crimson Text'
size_font=12
WHITE = '#EEEEEE'
BLUE = '#222831'


# -------------------------------------------------------------------------Password Generator-------------------------------------


# website, username, password
# -------------------------------------------------------------------------Save Password------------------------------------------
def generate_password():
    pass

def update_password():
    pass

def save_password(website, username, password, empty_file=False):
    if empty_file:
        with open('data.csv', mode='w') as file:
            file.write('website,username,password')

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

        pandas.DataFrame(data).to_csv('data.csv', mode='a', index=False, header=False)
        
        messagebox.showinfo(title='sylock: Password Manager', message="Beep. Boop. Beep. Your Password has been saved successfully.")


def check_password():
    website = e1.get()
    username = e2.get()
    password = e3.get()
    try:
        data = pandas.read_csv('data.csv')
    
    except:
        save_password(website, username, password, empty_file=True)
        
    else:
        website_list = data['website'].to_list()
        if website in website_list: 
            # If Current 'Website' is in DB,
            # check if the username is same, if it is
            # ask user if they want to update, if yes, go ahead. 
            if data[data.website == website].username == username:
                update_password(website, username, password)
            
    

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
b3.config(text='Generate Password', bg=BLUE, fg=WHITE, bd='5')
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