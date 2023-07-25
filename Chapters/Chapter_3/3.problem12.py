
# Create a turtle clock face

import turtle

nib = turtle.Turtle()
nib.speed(0)
nib.shape("turtle")
nib.pensize(4)
deg = 90

# main loop
for i in range(0,12):
    nib.hideturtle()
    nib.stamp()
    nib.left(deg)
    nib.penup()
    nib.forward(100)
    nib.pendown()
    nib.forward(25)
    nib.penup()
    nib.forward(25)
    nib.pendown()
    nib.stamp()
    nib.penup()
    nib.home()
    deg = deg+30

for i in range(0, 180):
    nib.hideturtle()
    nib.left(deg)
    nib.speed(100)
    nib.shape("circle")
    nib.shapesize(0.05,0.05)
    nib.penup()
    nib.forward(180)
    nib.pendown()
    nib.stamp()
    nib.penup()
    nib.home()
    deg = deg+2

turtle.done()