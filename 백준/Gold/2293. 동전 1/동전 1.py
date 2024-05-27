import sys

input = sys.stdin.readline

n, k = list(map(int, input().split()))

coins = [int(input()) for _ in range(n)]

memo = [0] * (k+1)
memo[0] = 1

for coin in coins:
    for i in range(1, k+1):
        if i < coin:
            continue

        memo[i] += memo[i-coin]

print(memo[-1])