from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    total_sum = sum1 + sum2
    if total_sum % 2 != 0:
        return -1

    q1 = deque(queue1)
    q2 = deque(queue2)
    
    for _ in range(len(q1) * 4):
        if sum1 > sum2:
            if len(q1) == 1:
                break
            value = q1.popleft()
            q2.append(value)
            sum1 -= value
            sum2 += value
                
        elif sum1 < sum2:
            if len(q2) == 1:
                break
            value = q2.popleft()
            q1.append(value)
            sum1 += value
            sum2 -= value
        else:
            break

        answer += 1

    if sum1 == sum2:
        return answer
    else:
        return -1