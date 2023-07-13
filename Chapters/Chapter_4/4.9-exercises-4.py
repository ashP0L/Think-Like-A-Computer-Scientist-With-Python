
# Draw the picture

import turtle
# turt init
rex = turtle.Turtle()
bg = turtle.Screen()
bg.bgcolor('lightgreen')

def draw_square(t,size):
    t = turtle.Turtle()
    t.hideturtle()
    t.width(2)
    t.color('blue')

    for i in range(18):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(90)
        t.forward(size*2)
        t.left(90)
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.left(18)

for i in range(20):
    draw_square(rex,100)

turtle.done()