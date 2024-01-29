
N = int(input())

dp = [[0] * N for _ in range(10)]

for i in range(1, 10):
    dp[i][0] = 1


for col in range(1, N):
    for row in range(10):
        if row - 1 >= 0:
            dp[row][col] += dp[row-1][col-1]
        if row + 1 < 10:
            dp[row][col] += dp[row+1][col-1]

total = 0
for i in range(10):
    total += dp[i][N-1]

print(total % 1000000000)