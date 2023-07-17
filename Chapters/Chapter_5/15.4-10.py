# Calculate the hypotnuse
from math import sqrt
def define_hypot(s1, s2):
    """Given two sides of a triangle, determines if it's a right triangle"""
    c = sqrt(s1**2 + s2**2)
    print(c)

define_hypot(5, 5)


