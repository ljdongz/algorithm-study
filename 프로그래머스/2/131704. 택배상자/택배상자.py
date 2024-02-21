from collections import deque

def solution(order):
    answer = 0

    stack = []
    order = deque(order)
    boxes = deque([i for i in range(1, len(order)+1)])

    
    while order:
        if boxes and order[0] > boxes[0]:
            stack.append(boxes.popleft())
        elif boxes and order[0] == boxes[0]:
            answer += 1
            boxes.popleft()
            order.popleft()
        else:
            if stack.pop() == order.popleft():
                answer += 1
            else:
                break

    return answer
