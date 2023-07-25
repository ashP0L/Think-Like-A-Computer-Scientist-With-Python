import turtle

# Turtle module brings two types: Turtle type and Screen type


playground_loop = turtle.Screen()

alex = turtle.Turtle()
alex.color("green")

# alex movement
# call the FORWARD method for the turtle.
# Methods are things that you can DO. You have and eat method and a sleep method.
alex.forward(50)
alex.left(30)
alex.backward(20)

playground_loop.mainloop()

