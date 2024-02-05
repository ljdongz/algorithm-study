import math

def isPrime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    count = 0

    startIndex = 0
    numString = ""

    while n != 0:
        numString = str(n % k) + numString
        n = n // k

    for i in range(len(numString)):
        if numString[i] != "0":
            continue
            
        num = int(numString[startIndex:i])
        startIndex = i

        if isPrime(num):
            count += 1
            
    if startIndex != len(numString) - 1:
        num = int(numString[startIndex:])

        if isPrime(num):
            count += 1

    return count
