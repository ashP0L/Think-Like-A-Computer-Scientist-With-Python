# Determine if a function is a right triangle.
# Requires 3 function args
# Return true if right angle, False if not

def mainloop():
    hypot = int(input("Enter the hypotenuse: "))
    lega = int(input("Enter leg a: "))
    legb = int(input("Enter leg b: "))
# Error check
    if hypot < (lega or legb):
        print("Remember, the longest side of the triangle is the hypotenuse. Please re-enter the legs.") # This is a terrible solution. Need to add exception handling so that the program can just select the hypotenuse automatically
    is_rightangled(lega, legb, hypot)
def is_rightangled(s1, s2, s3):
    """Tests if triangle has a right angle. Third input should be the longest side"""
    sumlegs = ((s1**2)+(s2**2))-(s3**2)
    if abs(sumlegs) > 0.000001: #approx equal to because of floating point innacuracy
        print("False")
    else:
        print("True")

mainloop()

# testvalues
# False: 13,6,11
# True: 17,15,8