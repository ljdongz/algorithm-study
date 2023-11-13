from collections import deque

def solution(progresses, speeds):
    answer = []
    
    isPop = False
    q = deque()

    for i in range(0, len(progresses)):
        q.append([progresses[i], speeds[i]])

    while q:
        count = 0
        for i in range(0, len(q)):

            if isPop and q[0][0] >= 100:
                q.popleft()
                count += 1
                continue

            if isPop and q[0][0] < 100:
                break

            q[i][0] += q[i][1]

        if isPop:
            answer.append(count)
            isPop = False

        if q and q[0][0] >= 100:
            isPop = True
        
    return answer