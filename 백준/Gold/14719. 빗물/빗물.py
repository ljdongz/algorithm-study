
import sys

input = sys.stdin.readline

row, col = list(map(int, input().split()))
rains = list(map(int, input().split()))

blocks = [[False] * col for _ in range(row)]

for c in range(col):
    for r in range(rains[c]):
        blocks[r][c] = True

result = 0

for r in range(row):
    cols = []
    for c in range(col):
        if blocks[r][c]:
            cols.append(c)

    if len(cols) > 1:
        for idx in range(len(cols)-1):
            result += cols[idx+1] - cols[idx] - 1

print(result)