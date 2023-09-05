n, m = map(int, input().split())

lst = []
for i in range(0, n):
  lst.append(0)

for i in range(0, m):
  x, y, z = map(int, input().split())
  for j in range(x - 1, y):
    lst[j] = z

for i in lst:
  print(i, end=" ")