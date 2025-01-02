import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))

products = [list(map(int, input().split())) for _ in range(N)]

memo = [[0] * (K+1) for _ in range(N+1)]

for i, product in enumerate(products):
    weight = product[0]
    value = product[1]

    for j in range(1, K+1):
        if j < weight:
            memo[i+1][j] = memo[i][j]
        else:
            memo[i+1][j] = max(memo[i][j], memo[i][j-weight] + value)

print(memo[-1][-1])
