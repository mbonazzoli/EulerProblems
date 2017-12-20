# Brett Graham
# Matthew Bonazzoli


def prime_factor():
    num = 1
    primeList = []
    while True:
        if len(primeList) == 1001:
            return primeList[-1]
        else:
            if isPrime(num):
                primeList += [num]
            num += 1


def isPrime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
        else:
            return True


print(prime_factor())