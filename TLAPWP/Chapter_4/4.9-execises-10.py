# Extend your program above. Draw five stars, but between each, pick up the pen, move
# forward by 350 units, turn right by 144, put the pen down, and draw the next star. You’ll
# get something like this:

import turtle

rex = turtle.Turtle()
rex.hideturtle()
bg = turtle.Screen()
bg.bgcolor('lightgreen')

def makestar():
    t = turtle.Turtle()
    t.pencolor('pink')
    t.width(3.5)
    t.speed(10)
    for i in range(5):
        t.pendown()
        for i in range(5):
            t.right(144)
            t.forward(100)
        t.penup()
        t.forward(350)
        t.right(144)
    #t.penup()

makestar()
turtle.done()