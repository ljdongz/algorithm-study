import sys

input = sys.stdin.readline

calc = input().rstrip().split("-")

answer = 0

for idx, cal in enumerate(calc):

    cal = cal.split("+")
    result = sum(list(map(int, cal)))
    
    if idx == 0:
        answer += result
    else:
        answer -= result


print(answer)