# Write the grading program

xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

def get_mark(g):
    mark = 0
    if g <= 39.999:
        mark = "F3"
    if (g >= 40) and (g <= 44.999):
        mark = "F2"
    if (g >= 45) and (g <= 49.999):
        mark = "F1 Supp"
    if (g >= 50) and (g <= 59.999):
        mark = "Third"
    if (g >= 60) and (g <= 69.999):
        mark = "Second"
    if (g >= 70) and (g <= 74.999):
        mark = "Upper second"
    if g >= 75:
        mark = "First"

    print("You scored: ",g,"\nYour mark is:", mark, "\n")

for i in xs:
    get_mark(i)