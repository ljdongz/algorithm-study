import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = list(map(int, input().split()))

graph = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
  a, b = list(map(int, input().split()))
  graph[a].append(b)
  graph[b].append(a)

flag = 0

def dfs(v, depth):
  global flag

  visited[v] = True

  if depth == 5:
    flag = 1
    return
  
  for next in graph[v]:
    if not visited[next]:
      dfs(next, depth + 1)
  
  visited[v] = False

for i in range(N):
  dfs(i, 1)
  if flag: break

print(flag)

"""
노드를 정수로 표현할 경우
인접 리스트를 딕셔너러가 아닌 배열로 구현 가능
- 딕셔너리
  graph = {
    0: [1, 2, 3],
    1: [0, 3],
    2: [0],
    3: [0, 1]
  }
- 배열
  graph = [
    [1, 2, 3],
    [0, 3],
    [0],
    [0, 1]
  ]
"""
