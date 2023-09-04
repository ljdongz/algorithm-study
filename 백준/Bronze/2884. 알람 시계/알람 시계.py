x, y = map(int, input().split())

y = y - 45
if y < 0:
  y = y + 60
  x = x - 1
  if x < 0:
    x = x + 24

print(x, y)