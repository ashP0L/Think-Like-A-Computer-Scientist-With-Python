    #Write a void function to draw a star, where the length of each side is 100 units. (Hint:
    #You should turn the turtle by 144 degrees at each point.)

import turtle

rex = turtle.Turtle()
rex.hideturtle()
bg = turtle.Screen()
bg.bgcolor('lightgreen')
def makestar(t):
    t = turtle.Turtle()
    t.pencolor('pink')
    t.width(3.5)
    t.speed(10)
    for i in range(5):
        t.right(144)
        t.forward(100)

makestar(rex)

turtle.done()
