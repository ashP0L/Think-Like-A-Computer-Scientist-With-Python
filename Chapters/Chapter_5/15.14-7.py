# Modify the turtle bar chart program so that the pen is up for the small gaps between each bar.

# turtle bar chart
import turtle

turt = turtle.Turtle()
turt.color("blue")
turt.width(4)
turt.fillcolor("red")
turt.hideturtle()
turt.speed(10)
# Graph values
graphValue = [100, 50, 20, 5, 100, 77, 54, 200, 205, 100]

# For drawGraph, I think I need to define parameters turtle and height

def drawGraph(t, height):
    """Draw the graph bars."""
    turt.left(90)
    turt.begin_fill()
    turt.forward(height)
    turt.right(90)
    turt.forward(9)
    turt.write(height)
    turt.forward(21)
    turt.right(90)
    turt.forward(height)
    turt.left(90)
    turt.end_fill()

def move_turtle(turt):
    turt.penup()
    turt.forward(10)
    turt.pendown()


for a in graphValue:
    drawGraph(turt, a)
    move_turtle(turt)


turtle.done()
