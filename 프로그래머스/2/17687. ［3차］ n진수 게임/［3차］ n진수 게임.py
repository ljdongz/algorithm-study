"""
n : 진법
t : 숫자
m : 참가 인원
p : 내 순서
"""

values = "0123456789ABCDEF"

def convert(n, num):
    if num == 0:
        return "0"
    div = num
    result = ""
    while div != 0:
        div, mod = divmod(div, n)
        result = values[mod] + result
    return result

def solution(n, t, m, p):
    answer = ''

    numString = ""
    numCount = 0
    while (len(numString) // m) < t:
        numString += convert(n, numCount)
        numCount += 1
    

    turn = p-1
    for _ in range(t):
        answer += numString[turn]
        turn += m

    return answer