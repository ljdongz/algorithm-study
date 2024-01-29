import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

table = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    table[i] = [0] + list(map(int, input().split()))

dp = [[0] * (N+1) for _ in range(N+1)]

for r in range(1, N+1):
    for c in range(1, N+1):
        dp[r][c] = dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1] + table[r][c]


for _ in range(M):
    x1, y1, x2, y2 = list(map(int, input().split()))

    print(dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1])

