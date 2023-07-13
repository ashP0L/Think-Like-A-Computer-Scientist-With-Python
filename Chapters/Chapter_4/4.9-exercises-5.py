# Make the shapes
# Reference pp. 51 question 5

import turtle

turt = turtle.Turtle()
turt.hideturtle()
bg = turtle.Screen()
bg.bgcolor('lightgreen')

def spiralrotate(functurt, n):
    functurt = turtle.Turtle()
    functurt.color('blue')
    functurt.width(3)
    functurt.speed(10)
    x = 0
    angle = 90
    for i in range(n):
        x = x+2.5
        angle = angle +
        functurt.right(angle)
        functurt.forward(x)

spiralrotate(turt, 200)

turtle.done()
