from collections import deque

def solution(n, computers):
    visited = [False] * n
    result = 0
    
    def bfs(index):
        q = deque()
        q.append(index)
        
        while q:
            cur = q.popleft()
            for idx in range(len(computers[cur])):
                if computers[cur][idx] == 1 and not visited[idx]:
                    q.append(idx)
                    visited[idx] = True
                    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            bfs(i)
            result += 1
            
    return result