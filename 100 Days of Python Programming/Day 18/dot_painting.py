import random

import colorgram
import turtle

# colors = colorgram.extract('image.jpg',34)
#
# for n in range(0, 34):
#     color = colors[n].rgb
#     color_list.append((color[0], color[1], color[2]))
#
# print(color_list)
color_list = [(233, 231, 219), (195, 160, 121), (134, 85, 64), (230, 237, 231), (67, 89, 115), (137, 63, 75),
              (225, 231, 238), (147, 162, 175), (217, 200, 146), (39, 43, 60), (60, 36, 47), (187, 144, 153),
              (238, 224, 229), (190, 97, 77), (59, 41, 33), (108, 43, 56), (163, 143, 69), (87, 104, 93),
              (48, 59, 91), (183, 94, 107), (148, 161, 153), (104, 48, 42), (38, 53, 45), (217, 180, 172),
              (220, 174, 181), (113, 136, 124), (118, 122, 147), (47, 74, 60), (104, 137, 142), (74, 70, 42),
              (42, 73, 80), (181, 190, 206), (176, 196, 203), (183, 197, 190)]


tim = turtle.Turtle()
turtle.colormode(255)

tim.pensize(20)
tim.speed(0)
positions = [-460,-350]

tim.penup()
tim.setposition(-460, -350)


def draw_art():
    for _ in range(19):
        tim.color(set_color())
        tim.pendown()
        tim.forward(1)
        tim.penup()
        tim.forward(50)


def set_position():
    positions[1] = positions[1] + 50
    tim.setposition(positions[0], positions[1])


def set_color():
    return random.choice(color_list)


for _ in range(15):
    draw_art()
    set_position()


screen = turtle.Screen()
screen.exitonclick()