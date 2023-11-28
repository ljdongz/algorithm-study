from itertools import permutations

def solution(numbers):
    answer = 0
    dict = {}

    for i in range(1, len(numbers) + 1):
        nPr = list(permutations(numbers, i))

        for nums in nPr:
            numString = ""

            for n in nums:
                numString += n
        
            num = int(numString)
            if num not in dict and isPrime(num):
                print(num)
                dict[num] = True
                answer += 1

    return answer

def isPrime(number):
    if number == 0 or number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True