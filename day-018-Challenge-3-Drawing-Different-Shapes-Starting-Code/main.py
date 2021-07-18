import random
import turtle as t

tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

##Var_1
# corner = 3
# colour = ["red", "orange", "yellow", "green", "blue", "dark blue", "violet", "sea green"]
# a = -1
# while corner <= 10:
#     b = a + 1
#     pen_colour = colour[b]
#     for step in range(corner):
#         tim.pencolor(pen_colour)
#         tim.right(360/corner)
#         tim.forward(100)
#     corner += 1
#     a = b


##Var#2
colour = ["red", "orange", "yellow", "green", "blue", "dark blue", "violet", "sea green"]


def drow_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.pencolor(random.choice(colour))
    drow_shape(shape_side_n)
