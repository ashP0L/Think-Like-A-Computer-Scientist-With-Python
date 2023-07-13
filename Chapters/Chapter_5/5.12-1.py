# turtle bar chart
import turtle

turt = turtle.Turtle()
turt.color("blue")
turt.width(4)
turt.fillcolor("red")
# Graph values
graphValue = [100,50, 20, 5, 100, 77, 54]

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
    turt.hideturtle()
    turt.forward(10)
    turt.showturtle()

for a in graphValue:
    drawGraph(turt, a)

turtle.done()
