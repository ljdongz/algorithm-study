n, m = map(int, input().split())

lst = [i for i in range(1, n + 1)]

for i in range(0, m):
  a, b = map(int, input().split())

  tmp = lst[a-1:b]
  tmp.reverse()
  lst[a-1:b] = tmp

for i in lst:
  print(i, end=' ')