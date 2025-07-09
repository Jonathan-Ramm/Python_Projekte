import math
from turtle import *

def star_x(angle, size):
    return size * math.cos((angle))**3

def star_y(angle, size):
    return size * math.sin((angle))**3

def draw_filled_star(size):
    # Set up the drawing
    speed(1000)
    bgcolor("black")
    color("yellow")

    penup()
    goto(star_x(0, size), star_y(0, size))
    pendown()

    # Draw the star
    for angle in range(5000):
        goto(star_x(angle, size), star_y(angle, size))
        goto(0, 0)

    done()

# Draw a filled star with a specified size
draw_filled_star(100)
