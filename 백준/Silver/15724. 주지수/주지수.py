import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

memo = [[0] * M for _ in range(N)]

population = [list(map(int, input().split())) for _ in range(N)]

memo[0][0] = population[0][0]

for i in range(1, N):
    memo[i][0] = memo[i-1][0] + population[i][0]
for j in range(1, M):
    memo[0][j] = memo[0][j-1] + population[0][j]
for i in range(1, N):
    for j in range(1, M):
        memo[i][j] = memo[i-1][j] + memo[i][j-1] + population[i][j] - memo[i-1][j-1]

k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = list(map(int, input().split()))

    result = memo[x2-1][y2-1]

    if x1 != 1 and y1 != 1:
        result -= (memo[x2-1][y1-2] + memo[x1-2][y2-1] - memo[x1-2][y1-2])
    elif x1 == 1 and y1 != 1:
        result -= memo[x2-1][y1-2]
    elif x1 != 1 and y1 == 1:
        result -= memo[x1-2][y2-1]
    
    print(result)