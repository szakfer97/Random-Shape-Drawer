import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.pencolor("white")
t.penup()
t.goto(0, 0)
t.pendown()

for _ in range(20):
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    angle = random.uniform(0, 360)
    t.setheading(angle)
    t.circle(100)

screen.mainloop()
