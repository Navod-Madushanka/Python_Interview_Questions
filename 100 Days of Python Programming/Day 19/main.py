import turtle
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']

screen = turtle.Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")+ "_turtle"
print(user_bet)

turtles = []

for color in colors:
    name = f"{color}_turtle"
    turtle_obj = turtle.Turtle(shape="turtle")
    turtle_obj.penup()
    turtle_obj.color(color)
    turtles.append({name: turtle_obj})


width = -230
height = 370
difference = height / len(turtles)
new_height = height / 2

for n in range(len(turtles)):
    turtle = list(turtles[n].values())[0]
    turtle.goto(width, new_height)
    new_height -= difference


is_game_on = False

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle_dict in turtles:
        turtle = list(turtle_dict.values())[0]
        if turtle.xcor() >= 240:
            if list(turtle_dict.keys())[0] == user_bet:
                print(f"You won. ")
            else:
                print(f"You lose.")
            print(f"The winner turtle is {list(turtle_dict.keys())[0]}")
            is_game_on = False
        else:
            turtle.forward(random.randint(0, 10))

screen.listen()

screen.exitonclick()
