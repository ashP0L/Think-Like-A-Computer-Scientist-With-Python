
# 6.9 exercises
from math import sqrt

# 1.
# The four compass points can be abbreviated by single-letter strings as “N”, “E”, “S”, and
# "W”. Write a function turn_clockwise that takes one of these four compass points
# as its parameter, and returns the next compass point in the clockwise direction.

# testing helper
import sys

def test(did_pass):
    """Print the result of a test"""
    lineenum = sys._getframe(1).f_lineno #Get call line number
    if did_pass:
        msg = "Test at line {0} ok".format(lineenum)
    else:
        msg = "Test at line {0} FAILED".format(lineenum)
    print(msg)


d = "W"
def turn_clockwise(n):
    if n == "N":
        return "E"
    elif n == "E":
        return "S"
    elif n == "S":
       return "W"
    elif n == "W":
        return "N"
print("Starting test for turn_clockwise... \n")
# Test scaffold for turn_clockwise
test(turn_clockwise("N") == "E")
test(turn_clockwise("W") == "N")
test(turn_clockwise("42") == None)
test(turn_clockwise("rubbish") == None)
print("Test for turn_clockwise completed. \n")

# 2
# Write a function day_name that converts an integer number 0 to 6 into the name of a
# day. Assume day 0 is “Sunday”. Once again, return None if the arguments to the function
# are not valid. Here are some tests that should pass:

def weekday(w):
    if w == 1:
        return  "Monday"
    if w == 2:
        return "Tuesday"
    if w == 3:
        return "Wednesday"
    if w == 4:
        return "Thursday"
    if w == 5:
        return "Friday"
    if w == 6:
        return "Saturday"
    if w == 7:
        return "Sunday"
    else:
        return None

print("Starting test for weekday... \n")

test(weekday(1) == "Monday")
test(weekday(3) == "Wednesday")
test(weekday("rubbish") == None)
test(weekday(42) == None)

print("Testing completed for weekday.\n")

#3 Write the inverse function day_num which is given a day name, and returns its number:

def day_num(d):
    if d == "Monday":
        return 1
    if d == "Tuesday":
        return 2
    if d == "Wednesday":
        return 3
    if d == "Thursday":
        return 4
    if d == "Friday":
        return 5
    if d == "Saturday":
        return 6
    if d == "Sunday":
        return 7
    else:
        return None

print("Starting test for day_num \n")

test(day_num("Friday") == 5)
test(day_num("Sunday") == 7)
test(day_num(weekday(3)) == 3) # fruit of day_num and weekday.
test(weekday(day_num("Wednesday")) == "Wednesday")
test(day_num("Wrong"))

print("\nTesting completed for day_num \n")

# 4.
# Write a function that helps answer questions like “‘Today is Wednesday. I leave on
# holiday in 19 days time. What day will that be?”’ So the function must take a day name
# and a delta argument — the number of days to add — and should return the resulting
# day name:

# && 5. 
# Can your day_add function already work with negative deltas? For example, -1 would
# be yesterday, or -7 would be a week ago:

def day_print(ya):
    if ya == 1:
        return "Monday"
    if ya == 2:
        return "Tuesday"
    if ya == 3:
        return "Wednesday"
    if ya == 4:
        return "Thursday"
    if ya == 5:
        return "Friday"
    if ya == 6:
        return "Saturday"
    if ya == 7:
        return "Saturday"
def day_add(day,x):
    if day == "Monday":
        d = 1
    elif day == "Tuesday":
        d = 2
    elif day == "Wednesday":
        d = 3
    elif day == "Thursday":
        d = 4
    elif day == "Friday":
        d = 5
    elif day == "Saturday":
        d = 6
    elif day == "Sunday":
        d = 7
    else:
        return None
    #Mod weekday
    if x >= 0:
        y = (d + x) % 7
    else:
        if x > -7:
            y = 7 - (7 - (abs(d + x))) # 7 minus abs operation because we're going backwards from sunday.
        else:
            y = (7 - (abs(d + x) % 7))
    return day_print(y)

print("\nStarting test for day_add and day_print\n")

test(day_add("Monday", 4) == "Friday")
test(day_add("Tuesday", 0) == "Tuesday")
test(day_add("Tuesday", 14) == "Tuesday")
test(day_add("Tuesday", -7) == "Tuesday")
test(day_add("Monday", -7) == "Tuesday")
test(day_add("Rubbish", -7) == "Tuesday")
test(day_add("Tuesday", -15) == "Monday")
test(day_add("Monday", -10) == "Friday")
test(day_add("Friday", -1) == "Thursday")

print("\nTesting completed for day_add and day_print\n")

# 6.
# Write a function days_in_month which takes the name of a month, and returns the
# number of days in the month. Ignore leap years:

def days_in_month(month):
    if month == "January":
        return 31
    elif month == "February":
        return 28
    elif month == "March":
        return 31
    elif month == "April":
        return 30
    elif month == "May":
        return 31
    elif month == "June":
        return 30
    elif month == "July":
        return 31
    elif month == "August":
        return 31
    elif month == "September":
        return 30
    elif month == "October":
        return 31
    elif month == "November":
        return 30
    elif month == "December":
        return 31
    else:
        return None
# test cass

print("\nStarting test for days_in_month\n")
test(days_in_month("February") == 28)
test(days_in_month("December") == 31)
test(days_in_month("Junk") == 31)
print("\nTesting for days_in_month complete\n")

# 7. Write a function to_secs that converts hours, minutes and seconds to a total number
# of seconds.

def to_secs(h,m,s):
    return ((h * 3600) + (m * 60) + (s))

print("\nStarting test for to_secs:\n")
test(to_secs(2, 30, 10) == 9010)
test(to_secs(2, 0, 0) == 7200)
test(to_secs(0, 2, 0) == 120)
test(to_secs(0, 0, 42) == 42)
test(to_secs(0, -10, 10) == -590)
print("\nTesting completed for to_secs\n")

# 8. Extend to_secs so that it can cope with real values as inputs. It should always return
# an integer number of seconds (truncated towards zero):

def to_secs_2(h,m,s):
    x = int(((h * 3600) + (m * 60) + (s))) # truncate towards zero with int()
    return x

print("\nStarting test for test_to_sec_2\n")
test(to_secs_2(2.5, 0, 10.71) == 9010)
test(to_secs_2(2.433, 0, 0) == 8758)
print("\nTesting completed for test_to_sec_2\n")

# 9. Write three functions that are the “inverses” of to_secs:
# (a) hours_in returns the whole integer number of hours represented by a total num-
# ber of seconds.
# (b) minutes_in returns the whole integer number of left over minutes in a total
# number of seconds, once the hours have been taken out.
# (c) seconds_in returns the left over seconds represented by a total number of sec-
# onds.

# 9(a)
def hours_in(s):
    return s // 3600 # refactored into floor division

def minutes_in(s):
    return (s % 3600) // 60 # refactored into floor division

def seconds_in(s):
    x = hours_in(s)
    y = minutes_in(s)
    return s % ((x * 3600)+(y * 60))

    print(x,y)

print("\nStarting test for question 9.")

test(hours_in(9010) == 2)
test(minutes_in(9010) == 30)
test(seconds_in(9010) == 10)

print("\nTest for question 9 completed.")

# 10. Which of these tests fail? Explain why.
print("\nStarting tests for question 10.\n")

test(3 % 4 == 0) # T
test(3 % 4 == 3) # T 3 - {(3/4} * 4
test(3 / 4 == 0) # F 3
test(3 // 4 == 0) # T - floor division = return 0
test(3+4 * 2 == 14) # F
test(4-2+2 == 0) # F
test(len("hello, world!") == 13) # T

print("\nTesting for question 10 completed.\n")

# 11. Write a compare function that returns 1 if a > b, 0 if a == b, and -1 if a < b

def compare(a,b):
    if a > b:
        return 1
    elif a == b:
        return 0
    elif a < b:
        return -1

print("\nStarting tests for compare\n")

test(compare(5, 4) == 1)
test(compare(7, 7) == 0)
test(compare(2, 3) == -1)
test(compare(42, 1) == 1)

print("\nTesting for compare completed\n")

# 12. Write a function called hypotenuse that returns the length of the hypotenuse of a right
# triangle given the lengths of the two legs as parameters:

def hypotenuse(a, b):
    return sqrt((a**2)+(b**2))

print("\nStarting tests for hypotenuse\n")

test(hypotenuse(3, 4) == 5.0)
test(hypotenuse(12, 5) == 13.0)
test(hypotenuse(24, 7) == 25.0)
test(hypotenuse(9, 12) == 15.0)

print("\nTesting for hypotenuse completed\n")

# 13. Write a function slope(x1, y1, x2, y2) that returns the slope of the line through
# the points (x1, y1) and (x2, y2). Be sure your implementation of slope can pass the
# following tests:

def slope(x1,y1,x2,y2):
    return ((y2-y1) / (x2-x1))

print("\nStarting tests for slope\n")

test(slope(5, 3, 4, 2) == 1.0)
test(slope(1, 2, 3, 2) == 0.0)
test(slope(1, 2, 3, 3) == 0.5)
test(slope(2, 4, 1, 2) == 2.0)

print("\nTesting for slope completed\n")

# Then use a call to slope in a new function named intercept(x1, y1, x2, y2)
# that returns the y-intercept of the line through the points (x1, y1) and (x2, y2)

def intercept(x1,y1,x2,y2):
    

test(intercept(1, 6, 3, 12) == 3.0)
test(intercept(6, 1, 1, 6) == 7.0)
test(intercept(4, 6, 12, 8) == 5.0)