
import datetime
import turtle

# 1. Print a program that prints "We Like Python Turtles!" 1,000 times

for i in range(1000):
        print("I really like turtles!")

# 2. Give three attributes of your cell phone project, give three
#   methods of your cell phone project.

# Attributes
    # screenmodel
    # size
    # OS
# Methods
    # roaming behavior
    # OTA update
    # biometric authentication

# 3.3. Write a program that uses a for loop to print
# One of the months of the year is January
# One of the months of the year is February

month_int = list(range(1,12))

for i in month_int:
    month = datetime.date(1999,i,9).strftime('%B')
    print("One of the months of the year is",month)


# 4. Suppose our turtle tess is at heading 0 — facing east. We execute the statement
# tess.left(3645). What does tess do, and what is her final heading?
#tess = turtle.Turtle()
#tess.position(0.00,0.00)
#tess.left(3645)

#print("Tess's heading is: ",tess.heading())
#turtle.done()

# 5. Loops

# Assume you have the assignment xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#   (a) Write a loop that prints each of the numbers on a new line.
#   (b) Write a loop that prints each number and its square on a new line.
#   (c) Write a loop that adds all the numbers from the list into a variable
#       called total. You should set the total variable to have the value 0
#       before you start adding them up, and print the value in total after
#       the loop has completed.
#   (d) Print the product of all the numbers in the list. (product means all
#       multiplied together)
xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]
total = 0
mul = 1

for number in xs:
    print(number)

for number in xs:
    print(number**2)

for number in xs:
    total=total+number

print(total)

for number in xs:
    mul *= number
print(mul)

#6. Use for loops to make a turtle draw these regular polygons (regular means all sides the
# same lengths, all angles the same):
# An equilateral triangle
# A square
# A hexagon (six sides)
# An octagon (eight sides)

turt1 = turtle.Turtle()

# E-Triangle
turt1.home()

#for i in range(3):
#    turt1.forward(40)
#   turt1.left(120)
#turtle.done()

# square
#turt1.home()

#for i in range(4):
#    turt1.forward(40)
#    turt1.left(90)

# Hexagon
# #turt1.home()

#for i in range(6):
#    turt1.forward(40)
#    turt1.left(60)
#turtle.done()

#for i in range(8):
#    turt1.forward(40)
#    turt1.left(45)
#    turtle.done()

#7.
#A drunk pirate makes a random turn and then takes 100 steps forward, makes another ran-
#dom turn, takes another 100 steps, turns another random amount, etc. A social science
#student records the angle of each turn before the next 100 steps are taken. Her experimen-
# tal data is [160, -43, 270, -97, -43, 200, -940, 17, -86]. (Positive
# angles are counter-clockwise.) Use a turtle to draw the path taken by our drunk friend.

#pirate = turtle.Turtle()
#angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]

#for x in angles:
#    pirate.forward(100)
#    pirate.left(x)

#turtle.done()

#8. Enhance your program above to also tell us what the drunk pirate’s heading is after he
# has finished stumbling around. (Assume he begins at heading 0).

#print(pirate.heading())

# 9. If you were going to draw a regular polygon with 18 sides, what angle would you need
# to turn the turtle at each corner?

# S = (n-2) * 180
# S / n

#angle = turtle.Turtle()

#for y in range(0,18):
#    angle.forward(50)
#    angle.left(20)

#turtle.done()

# 10.

# 11. Write a program that draws a 5 pronged star shape
rex = turtle.Turtle()
for i in range(0,5):
    rex.forward(40)
    rex.left(72)
    rex.right(288)
    rex.forward(40)
turtle.done()

triangle = turtle.Turtle()
for c in range(0,5):
    triangle.forward(50)
    triangle.left(168)
turtle.done()

# 12. Write a program to draw a face of a clock that looks something like this:

