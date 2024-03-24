import sys

input = sys.stdin.readline

N = int(input())

colors = input().rstrip()

answer = N

for c in ["B", "R"]:
    totalCount = 1
    diff = False

    for color in colors:
        # 비교하는 색상이랑 다를 경우
        if c != color:
            diff = True
        # 비교하는 색상이랑 같을 경우
        else:
            # 이전에 다른 색상이 나온 경우
            if diff:
                totalCount += 1
                diff = False
    
    if diff:
        totalCount += 1
    answer = min(answer, totalCount)

print(answer)
    