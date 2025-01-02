import sys

input = sys.stdin.readline

N = int(input())

starts = []
ends = []

for _ in range(N):
    s, e = list(map(int, input().split()))
    starts.append(s)
    ends.append(e)

starts.sort()
ends.sort()

result = 1
end_index = 0

for start_index in range(1, N):
    # 현재 시작 시간 >= 가장 빨리 끝나는 시간
    if starts[start_index] >= ends[end_index]:
        end_index += 1
    else:
        result += 1

print(result)