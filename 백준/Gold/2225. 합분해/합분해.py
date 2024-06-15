import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))

memo = [[0] * (N + 1) for _ in range(K)]

for i in range(N+1):
    memo[0][i] = 1

for i in range(K):
    memo[i][0] = 1

for i in range(1, K):
    for j in range(1, N+1):
        memo[i][j] = memo[i-1][j] + memo[i][j-1]

print(memo[-1][-1] % 1000000000)