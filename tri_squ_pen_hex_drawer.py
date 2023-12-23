import turtle
import random

# Function to draw a triangle


def form_tri(side):
    for i in range(3):
        my_pen.fd(side)
        my_pen.left(120)
        side -= 10

# Function to draw a square


def form_sq(side):
    for i in range(4):
        my_pen.fd(side)
        my_pen.left(90)
        side -= 5

# Function to draw a pentagon


def form_pen(side):
    for i in range(5):
        my_pen.fd(side)
        my_pen.left(72)

# Function to draw a hexagon


def form_hex(side):
    for i in range(6):
        my_pen.fd(side)
        my_pen.left(300)


# List of shape-drawing functions
shape_list = [form_tri, form_sq, form_pen, form_hex]

# Set up turtle screen
tut = turtle.Screen()
tut.bgcolor("black")
tut.title("Continous random drawing of triangles, squares, pentagons and hexagons")

# Create a turtle
my_pen = turtle.Turtle()
my_pen.color("white")
tut = turtle.Screen()
side = 120

# Draw 20 random shapes
for i in range(20):
    random.choice(shape_list)(side)
    my_pen.right(300)

# Finish drawing
turtle.done()
