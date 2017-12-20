# Brett Graham
# Matthew Bonazzoli
#
# Special Pythagorean triplet
# Problem 9
import math


def specPythagoreanTriplet():
     '''Finds the product of the unique a,b,c where a^2 + b^2 = c^2, and a,b, and c are all integers '''
     for a in range(500):
        for b in range(a):
            c = math.sqrt(a**2 + b**2)
            if a + b + c == 1000:
                return int(a*b*c)
     return 0


print(specPythagoreanTriplet())
