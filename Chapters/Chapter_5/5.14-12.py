# Determine if a function is a right triangle.
# Requires 3 function args
# Return true if right angle, False if not

# testvalues
# False: 13,6,11
# True: 17,15,8

def is_rightangled(s1, s2, s3):
    """Tests if triangle has a right angle. Third input should be the longest side"""
    sumlegs = ((s1**2)+(s2**2))-(s3**2)
    if abs(sumlegs) > 0.000001: #approx equal to because of floating point innacuracy
        print("False")
    else:
        print("True")

def mainloop():
    leg=[0, 1, 2]
    leg[0] = int(input("Enter the first leg: "))
    leg[1] = int(input("Enter the next leg: "))
    leg[2] = int(input("Enter the last leg: "))
# Prepare  list for is_rightangled
    leg.sort()


    print(leg[0],leg[1],leg[2])

    is_rightangled(leg[0], leg[1], leg[2])


mainloop()

