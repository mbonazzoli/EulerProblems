# Brett Graham
# Matthew Bonazzoli
#
# Factorial digit sum
# Problem 20

def factorial(x):
    """returns x!"""
    if x==0:
        return 1
    return x*factorial(x-1)


def sumDigits(x):
    '''Takes a number x and sums its digits'''
    sum = 0
    for i in range(len(x)):
        num = int(x[i])
        sum += num
    return sum
print(sumDigits(str(factorial(100))))