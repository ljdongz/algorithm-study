import sys

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * N for _ in range(N)]
DP[0][0] = 1

for row in range(N):
    for col in range(N):
        if (row, col) == (N-1, N-1):
            print(DP[row][col])
            break

        if DP[row][col] == 0:
            continue
        
        step = arr[row][col]

        if row + step < N:
            DP[row+step][col] += DP[row][col]
        if col + step < N:
            DP[row][col+step] += DP[row][col]
        
        
