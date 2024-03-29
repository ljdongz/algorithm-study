def solution(n):
    answer = ""

    number = ['1', '2', '4']
    
    while n > 0:
        n -= 1

        answer = number[n % 3] + answer

        n //= 3

    return answer


"""
수정 전

dict = {0: 1, 1: 2, 2: 4}

def solution(n):
    answer = ""
    
    numbers: list = []
    n -= 1

    if n in dict:
        return str(dict[n])

    while n >= 0:
        numbers.insert(0, n % 3)
        n = n // 3 - 1

    for num in numbers[:-1]:
        answer += str(dict[(num)])

    answer += str(dict[numbers[-1] % 3])

    return answer
"""
