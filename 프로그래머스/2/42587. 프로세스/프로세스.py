from collections import deque

def solution(priorities, location):
    answer = 0

    nowLocation = location # 알고싶은 프로세스 현재 위치
    isContinue = True

    q = deque(priorities)

    while isContinue:

        for i in range(len(q)):
            priority = q.popleft()

            if not q:
                isContinue = False
                answer += 1
                break

            if max(q) > priority:
                q.append(priority)
                if nowLocation == 0:
                    nowLocation = len(q)
            else:
                answer += 1
                if nowLocation == 0:
                    isContinue = False
                    break

            nowLocation -= 1

        
    return answer