import tkinter as tk

# Set up a window
window = tk.Tk()
window.title("Suyash's first GUI")
window.minsize(width=400, height=400)

# Creating a Label
label = tk.Label()
label.config(text="I am grateful.", font=("Roboto", 12, 'bold'))
label.grid(row=0, column=3)

# Creating a Button
button = tk.Button()
button['text'] = 'Click Me!'
button.grid(row=0, column=4)

def onclick_button():
    new_text = user_input.get()
    label['text'] = new_text
    print("I got clicked")


button['command'] = onclick_button

# Creating an entry
user_input = tk.Entry()
user_input['width'] = 30
user_input.insert(tk.END, string="type here...")
user_input.grid(row=1, column=3)

#Text
text = tk.Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(tk.END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", tk.END))
text.grid(row=3, column=3)

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = tk.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(row=5, column=0)


#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = tk.Scale(from_=0, to=100, command=scale_used)
scale.grid(row=5, column=2)

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tk.IntVar()
checkbutton = tk.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(row=7, column=0)

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tk.IntVar()
radiobutton1 = tk.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tk.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(row=7, column=1)
radiobutton2.grid(row=7, column=2)


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tk.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(row=9, column=3)
window.mainloop()



window.mainloop()
