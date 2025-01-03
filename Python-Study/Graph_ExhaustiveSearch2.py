from collections import deque

# BFS
def keysAndRooms_BFS(rooms):
  visited = [False for _ in range(len(rooms))] # 방문한 room 표시를 위한 초기화
  queue = deque() # 방문할 room을 저장할 큐
  queue.append(0) # 0번 방 추가

  while queue:
    cur_room = queue.popleft()
    visited[cur_room] = True
    for next_room in rooms[cur_room]: # 현재 방에 있는 key 순차 접근
      if not visited[next_room]:
        queue.append(next_room)

  if visited.__contains__(False): return False
  else: return True


# DFS
def keysAndRooms_DFS(rooms):
  visited = [False for _ in range(len(rooms))] # 방문한 room 표시를 위한 초기화
  
  def dfs(cur_room):
    visited[cur_room] = True
    for next_room in rooms[cur_room]:
      if not visited[next_room]:
        dfs(next_room)

  dfs(0) # 0번 방 부터 시작

  if visited.__contains__(False): return False
  else: return True

rooms = [[1,3],[3,0,2],[0], [0], [1]]

print(keysAndRooms_DFS(rooms))