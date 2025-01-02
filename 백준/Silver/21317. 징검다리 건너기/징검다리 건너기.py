import sys

input = sys.stdin.readline

N = int(input())

memo = [[999999] * 2 for _ in range(21)]
energy = [[0, 0] for _ in range(21)]

for i in range(N-1):
    energy[i+1] = list(map(int, input().split()))

k = int(input())

memo[1][0] = 0
memo[2][0] = energy[1][0]
memo[3][0] = min(memo[2][0] + energy[2][0], memo[1][0] + energy[1][1])

for i in range(4, N+1):
    memo[i][0] = min(memo[i-1][0] + energy[i-1][0], memo[i-2][0] + energy[i-2][1])
    memo[i][1] = min(memo[i-1][1] + energy[i-1][0], memo[i-2][1] + energy[i-2][1], k + memo[i-3][0])

print(min(memo[N][0], memo[N][1]))