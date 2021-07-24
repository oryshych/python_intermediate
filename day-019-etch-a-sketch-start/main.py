from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def move_lefts():
    tim.left(15)
def move_rights():
    tim.right(15)
def move_clear_home():
    tim.clear()
    tim.pen()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_lefts)
screen.onkey(key="d", fun=move_rights)
screen.onkey(key="c", fun=move_clear_home)


screen.exitonclick()
