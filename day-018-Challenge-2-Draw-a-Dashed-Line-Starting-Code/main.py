import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########

for step in range(50):
    tim.forward(2)
    tim.penup()
    tim.forward(2)
    tim.pendown()