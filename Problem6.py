# Brett Graham
# Matthew Bonazzoli


def sum_square_diff(num):
    sumSquare=0
    squareSum=0
    for i in range(1, num+1):
        sumSquare += i**2
        squareSum += i
    return (squareSum**2)-sumSquare


print(sum_square_diff(100))
