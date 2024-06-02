import sys

input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())

    coins = list(map(int, input().split()))

    M = int(input())

    memo = [0] * (M+1)
    memo[0] = 1

    for coin in coins:
        for i in range(1, M+1):
            if i < coin:
                continue

            memo[i] += memo[i-coin]

    print(memo[-1])