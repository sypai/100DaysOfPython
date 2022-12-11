from tkinter import *

window = Tk()
window.title('Unit Converter')
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

# GLOBAL VARIABLES
flag = 0 # 0 for Kg to Pound, 1 for Pound to Kg

# Labels
# Input Unit Label
label1 = Label()
label1.config(text="Kilograms", font=("Roboto", 12, 'bold'))
label1.grid(row=3, column=3)

# Label 'is equal to'
label2 = Label()
label2.config(text="is equal to", font=("Roboto", 10))
label2.grid(row=6, column=1)

# Label converted unit
label3 = Label()
label3.config(text='0 Pounds', font=("Roboto", 12, 'bold'))
label3.grid(row=6, column=2)
label3.config(padx=10, pady=20)

#Radiobutton
def radio1_used():
    global flag
    flag = 0
    radiobutton1.config(variable=radio_state)
    radiobutton1.config(variable=radio_state)
    label1.config(text="Kilograms", font=("Roboto", 12, 'bold'))
    label3.config(text='0 Pounds', font=("Roboto", 12, 'bold'))

def radio2_used():
    global flag
    flag = 1
    radiobutton2.config(variable=radio_state)
    radiobutton1.config(variable=radio_state)
    label1.config(text="Pounds", font=("Roboto", 12, 'bold'))
    label3.config(text='0 Kilograms', font=("Roboto", 12, 'bold'))

#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Kilograms to Pound", font=("Roboto", 14), value=1, command=radio1_used)
radiobutton2 = Radiobutton(text="Pound to Kilogram", font=("Roboto", 14), value=2, variable=radio_state, command=radio2_used)

radiobutton1.grid(row=0, column=1)
radiobutton2.grid(row=0, column=3)
radiobutton1.config(padx=10, pady=20)
radiobutton2.config(padx=10, pady=20)

# Entry
# Creating an entry
user_input = Entry()
user_input['width'] = 20
user_input.insert(END, string="0")
user_input.focus()
user_input.grid(row=3, column=2)


def convert():
    weight = float(user_input.get())
    if flag == 0:
        result = 2.20462262185 * weight
        label3.config(text=f"{str(result)} Pounds")

    if flag == 1:
        result = weight / 2.20462262185
        label3.config(text=f"{str(result)} Kilograms")
    

# Calculate Button
button = Button()
button.config(text='Convert', command=convert)
button.grid(row=8, column=2)

window.mainloop()