import sys

sys.setrecursionlimit(1000000)
T = int(input())

# Top Down

def topDown():
    
    def recursive(row, col):
        if col < 0:
            return 0

        if (row, col) not in memo:
            if row == 0:
                memo[(row, col)] = max(recursive(1, col - 1), recursive(1, col - 2)) + stickers[row][col]
            else:
                memo[(row, col)] = max(recursive(0, col - 1), recursive(0, col - 2)) + stickers[row][col]
        
        return memo[(row, col)]
        
    for _ in range(T):
        stickers = []
        memo = {}

        N = int(input())

        for _ in range(2):
            stickers.append(list(map(int, sys.stdin.readline().split())))
        
        print(max(recursive(0, N-1), recursive(1, N-1)))


topDown()


# Bottom Up

def bottomUp():
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
