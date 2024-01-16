import sys

T = int(input())

for _ in range(T):
    stickers = []

    N = int(input())

    for _ in range(2):
        stickers.append(list(map(int, sys.stdin.readline().split())))
    
    memo = [[0] * N for _ in range(2)]

    memo[0][0] = stickers[0][0]
    memo[1][0] = stickers[1][0]
    if N == 1:
        print(max(memo[0][0], memo[1][0]))
        continue

    memo[0][1] = stickers[1][0] + stickers[0][1]
    memo[1][1] = stickers[0][0] + stickers[1][1]
    if N == 2:
        print(max(memo[0][1], memo[1][1]))
        continue

    for i in range(2, N):
        memo[0][i] = stickers[0][i] + max(memo[1][i-1], memo[1][i-2])
        memo[1][i] = stickers[1][i] + max(memo[0][i-1], memo[0][i-2])

    print(max(memo[0][-1], memo[1][-1]))