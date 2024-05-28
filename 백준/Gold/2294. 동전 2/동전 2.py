import sys

input = sys.stdin.readline

n, k = list(map(int, input().split()))

coins = [int(input()) for _ in range(n)]
coins.sort()

memo = [0] * (k+1)

for coin in coins:
    for i in range(1, k+1):
        if i < coin:
            continue

        if i % coin == 0:
            memo[i] = memo[i-coin] + 1
        elif memo[i-coin] != 0:
            if memo[i] == 0:
                memo[i] = memo[i-coin] + 1
            else:
                memo[i] = min(memo[i-coin] + 1, memo[i])

if memo[-1] == 0:
    print(-1)
else:
    print(memo[-1])