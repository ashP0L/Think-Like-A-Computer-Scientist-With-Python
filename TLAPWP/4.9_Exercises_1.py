
import turtle

# screen and turtle init
bg = turtle.Screen()
bg.bgcolor('lightgreen')
rex = turtle.Turtle()
rex.pencolor('pink')
rex.pensize(4)

# move turtle
def rexmove():
    rex.forward(20)
    rex.left(90)
    rex.forward(20)
    rex.left(90)
    rex.forward(20)
    rex.left(90)
    rex.forward(20)
    rex.left(90)
    rex.penup()
    rex.forward(40)
    rex.pendown()
# Five squares, so need five loops
for i in range(5):
    rexmove()


turtle.done()