n, m = map(int, input().split())

lst = []
for i in range(1, n + 1):
  lst.append(i)

for i in range(0, m):
  a, b = map(int, input().split())
  tmp = lst.copy()

  for j in range(0, b - a + 1):
    lst[a - 1 + j] = tmp[b - 1 - j]
    
for i in lst:
  print(i, end=' ')