import sys

input = sys.stdin.readline

# 지페 금액
T = int(input()) 

# 동전 가지 수
k = int(input())

coins = [list(map(int, input().split())) for _ in range(k)]
coins.sort()

dp = [[0] * (T + 1) for _ in range(len(coins) + 1)]
dp[0][0] = 1

for row, (coin, count) in enumerate(coins):
    for col in range(T+1):
        c = 0
        while coin * c <= col and c <= count:
            dp[row+1][col] += dp[row][col - (coin * c)]
            c += 1
                
print(dp[-1][-1])