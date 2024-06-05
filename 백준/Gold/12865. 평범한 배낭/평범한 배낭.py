import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))

products = []

for _ in range(N):
    products.append(list(map(int, input().split()))) 
    
products.sort()

memo = [[0] * (K+1) for _ in range(N+1)]

maxValue = 0

for row, product in enumerate(products):
    weight = product[0]
    value = product[1]

    for col in range(1, K+1):
        if col < weight:
            memo[row+1][col] = memo[row][col]
        elif col == weight:
            memo[row+1][col] = max(memo[row][col], value)
        else:
            if memo[row][col - weight] != 0:
                memo[row+1][col] = max(memo[row][col - weight] + value, memo[row][col])
            else:
                memo[row+1][col] = memo[row][col]
                
        maxValue = max(maxValue, memo[row+1][col])

print(maxValue)