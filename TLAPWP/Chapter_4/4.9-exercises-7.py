# Write a fruitful function sum_to(n) that returns the sum of all integer numbers up to
# and including n. So sum_to(10) would be 1+2+3...+10 which would return the value
# 55.

def add_series(n):
    add = 0
    for i in range(n+1):
        add = add+i
    print(add)

add_series(10)
