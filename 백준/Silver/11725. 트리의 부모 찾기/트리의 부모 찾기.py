import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N = int(input())

nodes = [list(map(int, input().split())) for _ in range(N-1)]

dict = defaultdict(list)
q = deque()
q.append(1)

parents = [0] * (N + 1)
visited = [False] * (N + 1)

for i in range(len(nodes)):
  node = nodes[i]

  dict[node[0]].append(node[1])
  dict[node[1]].append(node[0])

while q:
  v = q.popleft()
  visited[v] = True

  lst = dict[v]
  for i in range(len(lst)):
    next = lst[i]
    if not visited[next]:
      q.append(next)
    else:
      parents[v] = next

for i in range(2, len(parents)):
  print(parents[i])