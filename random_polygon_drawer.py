import turtle
import random

def draw_polygon(noSides):
    
    internalAngles = ((noSides - 2) * 180) / noSides
    externalAngles = 180 - internalAngles
    for i in range(noSides):
        my_pen.forward(100)
        my_pen.left(externalAngles)
    my_pen.right(externalAngles)

tut = turtle.Screen()
tut.bgcolor("black")
tut.title("Continuous random drawing of polygons with sides from 3 to 10")

my_pen = turtle.Turtle()
my_pen.color("white")

for i in range(30):
    draw_polygon(random.randint(3, 10))

turtle.mainloop()
