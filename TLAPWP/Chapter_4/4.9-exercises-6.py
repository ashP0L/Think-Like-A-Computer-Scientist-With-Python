# Call draw_poly to draw an equilateral traingle.
import turtle

turt = turtle.Turtle()
turt.hideturtle()
bg = turtle.Screen()
bg.bgcolor('lightgreen')
def draw_poly(t, n, sz):
    t = turtle.Turtle()
    t.color('blue')
    t.width(3)

    for i in range(n):
        t.forward(sz)
        t.left(360/n)

def draw_triangle(t,sz):
    draw_poly(t, 3, sz)

draw_triangle(turt, 30)

turtle.done()