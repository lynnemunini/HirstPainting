# Extract 10 colors from an image.
from turtle import Turtle, Screen
import random
import colorgram
screen = Screen()
tim = Turtle()
tim.shape("circle")
tim.color("white")
tim.shapesize(1)
screen.colormode(255)
my_start = (-220, 220)
tim.penup()
tim.setx(my_start[0])
tim.sety(my_start[1])
tim.pendown()

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.
colors = colorgram.extract('image.jpg', 100)
color = []

for each in colors:
    rgb = each.rgb
    color.append(rgb)
# print(color)
# To display the colors as a tuple without rgb

color = [tuple(rgb) for rgb in color]
# print(color)


def draw(space, x):
    for i in range(x):
        for j in range(x):
            # dot
            tim.color(random.choice(color))
            tim.dot(20)

            # distance for another dot
            tim.forward(space)
        tim.backward(space * x)

        # direction
        tim.right(90)
        tim.forward(space)
        tim.left(90)


# Main Section
tim.penup()
draw(30, 15)

# hide the turtle
tim.hideturtle()

screen.exitonclick()

