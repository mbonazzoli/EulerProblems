# Brett Graham
# Matthew Bonazzoli
# Multiples of 3 and 5
# Problem 1

def determineMultiples_3or5(x):
    '''Returns a list of all the multiples of 3 or 5 that are smaller than x'''
    list = []
    for i in range(1,x):
        if i%3 ==0 or i%5==0:
            list.append(i)
    return list

def sumUpList(list):
    sum = 0
    for i in list:
        sum +=i
    return sum

print(determineMultiples_3or5(1000))
print(sumUpList(determineMultiples_3or5(1000)))