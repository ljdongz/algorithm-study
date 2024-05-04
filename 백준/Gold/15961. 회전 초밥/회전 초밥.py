import sys

input = sys.stdin.readline

# 접시 수, 초밥 가짓 수, 연속해서 먹는 접시 수, 쿠폰 번호
N, d, k, c = list(map(int, input().split()))

sushi_count = [0] * (d+1)

sushies = [int(input()) for _ in range(N)]

start = 0
end = k-1

cur_count = 0
result = 0

for i in range(k):
    sushi_count[sushies[i]] += 1
    if sushi_count[sushies[i]] == 1:
        cur_count += 1

for i in range(N-1):
    
    sushi_count[sushies[start]] -= 1
    if sushi_count[sushies[start]] == 0:
        cur_count -= 1

    sushi_count[sushies[(end+1) % N]] += 1
    if sushi_count[sushies[(end+1) % N]] == 1:
        cur_count += 1

    start += 1
    end += 1

    if cur_count >= result:
        if sushi_count[c] == 0:
            result = cur_count + 1
        else:
            result = cur_count

print(result)