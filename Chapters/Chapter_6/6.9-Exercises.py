
# 6.9 exercises

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
print("Test for turn_clockwise completed. \n\n")

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

print("Testing completed for weekday.\n\n")

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

print("\nTesting completed for day_num \n\n")

#4
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
    y = ((d + x) % 7)
    return day_print(y)

print("\nStarting test for day_add and day_print")

test(day_add("Monday", 4) == "Friday")
test(day_add("Tuesday", 0) == "Tuesday")
test(day_add("Tuesday", 14) == "Tuesday")
test(day_add("Sunday", 100) == "Tuesday")
test(day_add("Sunday", -100) == "Sunday")


print("\nTesting completed for day_add and day_print\n\n")