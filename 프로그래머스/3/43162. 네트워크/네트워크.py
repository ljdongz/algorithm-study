from collections import deque

def solution(n, computers):
    answer = 0

    visited = [False for _ in range(n)]

    def bfs(num):
        visited[num] = True
        q = deque()
        q.append(num)

        while q:
            cur = q.popleft()

            for i in range(n):
                if i == cur or computers[cur][i] == 0:
                    continue
                
                if not visited[i]:
                    q.append(i)
                    visited[i] = True

    for i in range(n):
        if visited[i]:
            continue
        else:
            answer += 1
            bfs(i)


    return answer