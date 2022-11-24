# import colorgram
from turtle import Turtle, Screen
import random

# colors = colorgram.extract('image.jpg', 20)

# color_list = []
# for color in colors:
    
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
    
#     color_list.append((r, g, b))

# print(color_list)

colors = [(194, 166, 108), (135, 167, 193), (49, 102, 145), (145, 90, 43), (10, 21, 54), (188, 156, 34), (224, 208, 115), (62, 23, 10), (184, 141, 165), (69, 119, 79), (59, 13, 24), (138, 180, 149), (135, 28, 13), (129, 77, 104), (14, 41, 25), (19, 53, 135)]

t = Turtle()
t.speed(0)
t.ht()

screen = Screen()
screen.colormode(255)

radius = 75
angle = 30
count = int(360 / angle)

for _ in range(5):
    t.pu()
    t.sety(-radius)

    for x in range(count):
        t.pd()
        t.dot(30, random.choice(colors))

        t.pu()
        t.setx(0)
        t.sety(-radius)
        t.seth(0)

        t.pu()
        t.circle(radius, (x+1)*angle)

    radius += 75


screen.exitonclick()