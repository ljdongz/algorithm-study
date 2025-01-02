import sys

input = sys.stdin.readline

N = int(input())

colors = input().rstrip()

reds = [c for c in colors.split("R") if c]
blues = [c for c in colors.split("B") if c]

result = min(len(reds), len(blues)) + 1
print(result)