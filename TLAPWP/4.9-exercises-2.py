
# Draw the squares

import turtle

# turtle and bg init
turtbg = turtle.Screen()
turtbg.bgcolor('lightgreen')

rex = turtle.Turtle()
rex.pencolor('pink')
rex.pensize(4)

def squareRepeat():
    x = 0

    for i in range(5):
        x = x+20
        rex.forward(20+x)
        rex.left(90)
        rex.forward(20+x)
        rex.left(90)
        rex.forward(20+x)
        rex.left(90)
        rex.forward(20+x)
        rex.penup()
        rex.forward(10)
        rex.left(90)
        rex.backward(10)
        rex.pendown()

squareRepeat()
turtle.done()
