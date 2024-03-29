"""Euler Problem  #2: Even Fibonacci numbers"""
'''Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the
 first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ... By considering the terms in the Fibonacci sequence whose
  values do not exceed four million, find the sum of the even-valued terms.'''


def fibNum():
    i = 0
    j = 1
    fib = 0
    sum = 0
    while True:
        fib = i + j
        i = j
        j = fib
        if fib > 4000000:
            return sum
        if fib % 2 == 0:
            sum += fib


print fibNum()
