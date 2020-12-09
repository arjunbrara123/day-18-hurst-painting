import colorgram
from random import choice
from turtle import Turtle, Screen

# Extract colours
cols = colorgram.extract('hirst-spot-painting.jpg', 10)
colours = []
for i in cols:
    # Ensure we are not storing background shades of white, only spot colours we want to recreate
    if int(i.rgb.r) < 230 or int(i.rgb.g) < 230 or int(i.rgb.b) < 230:
        colours.append((int(i.rgb.r), int(i.rgb.g), int(i.rgb.b)))

# Initialise object references
t = Turtle()
s = Screen()

# Initial Turtle Window graphics setup
t.pensize(20)
t.speed("fastest")
s.colormode(255)

# Loop through all squares
for x in range(10):
    for y in range(10):

        # Move to next square and set random colour
        t.penup()
        t.setpos(x * 50 - 250, y * 50 - 250)
        rand_colour = choice(colours)
        t.pencolor(rand_colour)
        t.pendown()
        t.forward(1)

# Keep Turtle window on screen until user clicks to exit
s.exitonclick()
