import turtle
import random

# Function to draw a polygon with a given number of sides


def draw_polygon(noSides):
    # Calculate the internal and external angles of the polygon
    internalAngles = ((noSides - 2) * 180) / noSides
    externalAngles = 180 - internalAngles

    # Draw the polygon
    for i in range(noSides):
        my_pen.forward(100)
        my_pen.left(externalAngles)

    # Adjust the turtle's orientation for the next polygon
    my_pen.right(externalAngles)


# Set up turtle screen
tut = turtle.Screen()
tut.bgcolor("black")
tut.title("Continuous random drawing of polygons with sides from 3 to 10")

# Create a turtle

my_pen = turtle.Turtle()
my_pen.color("white")

# Draw 30 polygons with sides randomly chosen between 3 and 10

for i in range(30):
    draw_polygon(random.randint(3, 10))

# Finish drawing
turtle.done()
