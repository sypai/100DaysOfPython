from turtle import Screen, Turtle
import pandas as pd

# Setting the screen
screen = Screen()
image = 'blank_states_img.gif'
screen.addshape(image)
map = Turtle()
map.shape(image)

t = Turtle()
t.ht()
t.pu()

# Reading the CSV File
data = pd.read_csv('50_states.csv')

game_is_on =  True
while game_is_on:
    user_input = screen.textinput("Statesgame!", "Name a state from the United States of America").capitalize()
    # Getting row where state is user_input
    row = data[data.state == user_input]

    if not row.empty:
        t.goto(int(row.x), int(row.y))
        t.write(user_input)
   


screen.exitonclick()