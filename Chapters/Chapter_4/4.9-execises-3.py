# Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular
# polygon. When called with draw_poly(tess, 8, 50), it will draw a shape like
# this: Pictured is a octagon

import turtle

# turtle init

tess = turtle.Turtle()  # I initially defiend tess as a global variable. I don't think I need this, as the turtle generation can be handled by functions params.
bg =turtle.Screen()
bg.bgcolor('lightgreen')

# main

def draw_poly(t, n, sz):
    t = turtle.Turtle()
    t.color('blue')
    t.width(4)
    # Angle handler
    angle = 360/n
    for i in range(n):
        t.forward(sz)
        t.left(angle)

draw_poly(tess,12,40)

turtle.done()
