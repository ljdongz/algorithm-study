import math

def solution(n,a,b):
    answer = 1

    while abs(a - b) != 1 or max(a, b) % 2 != 0:

        a = math.ceil(a / 2)
        b = math.ceil(b / 2)
        answer += 1

    return answer