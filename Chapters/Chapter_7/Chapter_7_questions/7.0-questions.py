# Chapter 7 exercises
import turtle

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

# 8 8. Trace the execution of the last version of print_mult_table and figure out how it
# works.

print("\n Print_mult_table executes as follows:")
print("\n\t1. Int n is defined at start of execution.\n\t ")
print("\n\t2. The function will loop for each number in i (10), multiplying n by i and printing the result. ")

# 9  Write a function print_triangular_numbers(n) that prints out the first n tri-angular numbers.
print("\nStarting question 9.")
def print_triangles(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
        print(i, "\t", sum)

print_triangles(5)

print("\nQuestion 9 completed.")

# 10 Write a function, is_prime, which takes a single integer argument and returns True
# when the argument is a prime number and False otherwise.
print("\nStarting question 10.")
def is_prime(n):
    if n % 2 == 1:
        return True
    else:
        return False

test(is_prime(11))
test(not is_prime(35))
test(is_prime(19911121))

print("\nQuestion 10 completed.")

print("\nStarting question 14.\n")
def num_digits2(x):
    n = abs(x)
    count = 0
    if n == 0:
        return 1
    while n != 0:
        count = count + 1
        n = n // 10
        print(n)
    return count


test(num_digits2(0) == 1)
test(num_digits2(-12345) == 5)