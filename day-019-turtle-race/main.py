from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []


vertical = -125
for turtle in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.setposition(-230, vertical)
    vertical +=50
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You win, {win_color} turtle is win")
            else:
                print(f"You lose, {win_color} turtle is win")

        turtle_step = random.randint(0, 10)
        turtle.forward(turtle_step)

screen.exitonclick()