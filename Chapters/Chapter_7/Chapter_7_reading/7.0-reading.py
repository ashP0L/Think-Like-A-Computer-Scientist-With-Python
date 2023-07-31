# Chapter 7 examples from chapter reading
import sys

# Unit test
def test(did_pass):
    """Print the result of a test"""
    lineenum = sys._getframe(1).f_lineno #Get call line number
    if did_pass:
        msg = "Test at line {0} ok".format(lineenum)
    else:
        msg = "Test at line {0} FAILED".format(lineenum)
    print(msg)

# 7.1 Assignment
test_variable_1 = 5
print(test_variable_1)
test_variable_1 = 140
print(test_variable_1, "\n")

# 7.2 Updating variables
n = 5
n = 5 + 10

# 7.3 Updating variable within for loop
def mysum(xs):
    """sum all the numbers in list xs, then return the total"""
    running_total = 0
    for x in xs: # For x elements in list xs
        running_total = running_total+x
    return running_total

print("\nStarting test for mysum\n")
test(mysum([1, 2, 3, 4]) == 10)
test(mysum([1.25, 2.5, 1.75]) == 5.5)
test(mysum([1, -2, 3]) == 2)
test(mysum([ ]) == 0)
test(mysum(range(11)) == 55)
print("\nTest for mysum completed\n")

# 7.4 the while statement
def sum_to(n):
    """Return the sum of  1 + 2 + 3 ... n"""
    ss = 0
    v = 1
    while v <= n:
        ss = ss + v
        v = v +1
    return ss

print("\nStarting test for sum_to")
test(sum_to(4) == 10)
test(sum_to(1000) == 500500)
print("\nTest completed for sum_to\n")


# 7.7
def num_digits(n):
    count = 0
    while n != 0:
        count = count + 1
        n = n // 10
    return count

print("\nStarting test for num_digits\n")
test(num_digits(710) == 3)
test(num_digits(1124) == 4)
test(num_digits(710) == 3)
print("\nTest for num_digits completed\n")

# 7.8 Abbreviated assignment

count = 0
count += 1
count += 3
count -= 4

# 7.10 tables
print("\nSquare root table")
for i in range(2, 10):
    print(i, "\t", i**2)



