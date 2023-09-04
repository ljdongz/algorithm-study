x, y = map(int, input().split())

h = int(input())

y = y + h
if y >= 60:
  a = y // 60
  y = y - (60 * a)
  x = x + a
  if x >= 24:
    b = x // 24
    x = x - (24 * b)

print(x, y)