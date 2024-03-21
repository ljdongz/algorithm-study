import sys

input = sys.stdin.readline

N = int(input())

drinks = list(map(int, input().split()))

maximum = max(drinks)

result = 0

for drink in drinks:
    if drink == maximum:
        result += drink
    else:
        result += drink / 2

print(result)