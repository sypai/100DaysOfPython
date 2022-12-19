from tkinter import *
import pandas as pd
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
FONT_1 = 'Roboto'
FONT_2 = 'Montserrat'
FONT_3 = 'Helvetica Neue'
SIZE_1 = 40
SIZE_2 = 60

current_card = {}
to_learn = {}

try:
    data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pd.read_csv('./data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:    
    to_learn = data.to_dict(orient="records")



# =================== Fetching Data and Showing on the card ===================
def fetch_new_word():
    global current_card, flip_timer
    
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    
    french_mot = current_card['French']

    canvas.itemconfig(canvas_image, image=front_img)
    canvas.itemconfig(language, text='French', fill="black")
    canvas.itemconfig(word, text=french_mot, fill="black")
    
    window.after(3000, func=flip_card)

def fetch_new_word_remove_current_word():
    # Since User knows this word, remove this from the list for future
    to_learn.remove(current_card)
    updated_df = pd.DataFrame(to_learn)
    updated_df.to_csv('./data/words_to_learn.csv', index=False)
    fetch_new_word()
    
def flip_card():
    global current_card
    english_word = current_card['English']

    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(language, text='English', fill="white")
    canvas.itemconfig(word, text=english_word, fill="white")


# =================== UI ===================
window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

## ----------- Canvas ------------
canvas = Canvas(width=800, height=528, bg=BACKGROUND_COLOR, highlightthickness=0)

front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')

canvas_image = canvas.create_image(400, 264, image=front_img)

### Row 0
# 'Language' Text in Canvas
language = canvas.create_text(400, 150, text='', font=(FONT_1, SIZE_1, 'italic'))
canvas.grid(row=0, column=0, columnspan=2)

# 'Word' Text in Canvas
word = canvas.create_text(400, 263, text='', font=(FONT_2, SIZE_2, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

### Row 1
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=fetch_new_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=fetch_new_word_remove_current_word)
right_button.grid(row=1, column=1)

fetch_new_word()

window.mainloop()