# Chapter 7 exercises

# Test suite
import sys

def test(did_pass):
    """Print the result of a test"""
    lineenum = sys._getframe(1).f_lineno #Get call line number
    if did_pass:
        msg = "Test at line {0} ok".format(lineenum)
    else:
        msg = "Test at line {0} FAILED".format(lineenum)
    print(msg)

# 1. Write a function to count how many odd numbers are in a list.
def count_odds(x):
    count = 0
    for num in x:
        if num % 2 == 1:
            count += 1
        else:
            pass
    return count
print("Starting test for count_odds...\n")

test(count_odds([3, 4, 5]) == 2)
test(count_odds([3, 4, 6]) == 1)
test(count_odds([3, 4, 6]) == 5) # FAILED

print("\nTesting complete for count_odds.\n")

# 2. Sum up all the even numbers in a list.
def sum_evens(x):
    sum = 0
    for num in x:
        if num % 2 == 0:
            sum += num
        else:
            pass
    return sum

print("Starting test for sum_evens...\n")

test(sum_evens([2, 4, 6]) == 12) # pass
test(sum_evens([2, 4, 5]) == 6) # pass
test(sum_evens([1, 3, 7]) == 0) # pass
test(sum_evens([1, 3, 7]) == 1) # Fail

print("\nTesting complete for sum_evens.\n")

# 3.  Sum all negative numbers in a list.
def sum_negatives(x):
    total = 0
    for n in x:
        if n <= 0:
            total += n
        else:
            pass
    return total

print("Starting test for sum_negatives...\n")

test(sum_negatives([-1, 2, -1]) == -2) # pass
test(sum_negatives([2, 1, 6, -100]) == -100) # pass
test(sum_negatives([-1,-10,-15]) == -26) # pass
test(sum_negatives([-1]) == 2) # fail

print("\nTesting for sum_negatives completed.\n")

# 4. Count how many words in a list have length 5.
# Could add functionality here to choose the word length.
# Try a v2 version that inserts words into a list by identifying them with a " " delineator... maybe...
def count_word_length(x):
    num = 0
    for word in x:
        if len(word) == 5:
            num += 1
        else:
            pass
    return num

print("\nStarting test for count_word_length...\n")

test(count_word_length(["no", "happy"]) == 1) # pass
test(count_word_length(["no", "happy", "sadly"]) == 2) # pass
test(count_word_length(["no", "happy"]) == 2) # fail

print("\nTesting for count_word_length completed.\n")

# 5. Sum all the elements in a list up to but not including the first even number. (Write your
# unit tests. What if there is no even number?)
def sum_all_evens(x):
    count = 0
    for num in x:
        if num % 2 == 0:
            break
        else:
            count += num
    print(count)
    return count

print("Starting test for sum_all_evens...\n")

test(sum_all_evens([1, 1, 1, 2]) == 3)
test(sum_all_evens([1, 1, 1]) == 3) # If no evens, the function won't break, and all elements of the list will be added.
test(sum_all_evens([1, 2, 1, 2]) == 1)

print("\nTesting for sum_all_evens completed.\n")

# 6. Count how many words occur in a list up to and including the first occurrence of the word
# “sam”. (Write your unit tests for this case too. What if “sam” does not occur?)

def find_sam(x):
    count = 0
    for word in x:
        if word == "sam":
            break               # Break statement occurs FIRST, so that no additional words are counted beyond "sam"
        else:
            count += 1
    return count

print("Starting test for find_sam...\n")

test(find_sam(["bill", "bob", "james", "sam"]) == 3)
test(find_sam(["james", "billy"]) == 2)
test(find_sam(["sam", "james"]) == 0)

print("\nTesting for find_sam completed.\n")

# 7. Add a print function to Newton’s sqrt function that prints out better each time it is
# calculated. Call your modified function with 25 as an argument and record the results.

def sqrt(n):
    approx = n /2.0
    while True:
        better = (approx + n/approx)/2.0
        if abs(approx - better) < 0.001:
            return better
        approx = better
        print("Better...", better)
print(sqrt(25.0))
print(sqrt(81))
test(sqrt(25.0) == 5.00)

# 8 
""""""