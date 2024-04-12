
import sys

input = sys.stdin.readline

N = int(input())

schedules = [list(map(int, input().split())) for _ in range(N)]
schedules.sort()
dates = [0] * 366

start = -1
end = -1
cur_max = 0 # 현재 최대 중첩

result = 0

for s, e in schedules:
    if s > end + 1:
        # 코팅지 넓이 계산
        result += (end - start + 1) * cur_max
        
        cur_max = 1
        start = s
        end = e
    
    end = max(end, e)
    for i in range(s, e+1):
        dates[i] += 1
        if cur_max < dates[i]:
            cur_max = dates[i]

result += (end - start + 1) * cur_max

print(result)