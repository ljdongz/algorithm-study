import sys

N, M = list(map(int, sys.stdin.readline().split()))

dp = [0] * (N + 1)

dp[1] = 1

for i in range(2, N+1):
    dp[i] = dp[i-1] * i

print(dp[N] // (dp[M] * dp[N-M]))
