from collections import deque

def solution(n, computers):
    answer = 0

    visited = [False for _ in range(n)] # 컴퓨터 방문 정보

    # num = 컴퓨터 번호(인덱스)
    def bfs(num):
        visited[num] = True
        q = deque()
        q.append(num)

        while q:
            cur = q.popleft()

            # 다음 방문할 컴퓨터 탐색
            for i in range(n):
                # 방문할 컴퓨터가 자기 자신이거나, 없는 경우 건너뛰기
                if i == cur or computers[cur][i] == 0:
                    continue
                
                # 방문하지 않은 컴퓨터인 경우
                if not visited[i]:
                    q.append(i)
                    visited[i] = True

    # 컴퓨터 개수만큼 반복
    for i in range(n):
        # 이미 방문한 컴퓨터면 건너뛰기
        if visited[i]:
            continue
        # 방문하지 않은 컴퓨터면 네트워크 개수 1증가 및 bfs 시작
        else:
            answer += 1
            bfs(i)

    return answer