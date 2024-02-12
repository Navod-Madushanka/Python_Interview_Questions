import turtle
import pandas as pd

# Load the CSV file into a pandas DataFrame
states_df = pd.read_csv("50_states.csv")
state_list = states_df["state"].tolist()
print(state_list)

# Set up the turtle screen and image
screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

for n in range(49, 0, -1):
    # Ask the user to input a state name
    user_input = screen.textinput(f"{n + 1}/50 Guess the state", "What's another state's name?").title()
    if user_input in state_list:
        row = states_df[states_df.state == user_input]
        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(row["x"].iloc[0], row["y"].iloc[0])
        new_turtle.write(user_input)

# Keep the turtle window open until the user closes it
turtle.mainloop()
