
from collections import deque

def solution(s):
    answer = 0
    
    if len(s) % 2 == 1: return answer

    queue = deque(list(s))
    stack = []

    for _ in range(len(s)):
        stack = []
        copyQueue = queue.copy()

        for _ in range(len(s)):
            value = copyQueue.popleft()
            if value == "(":
                stack.append(")")
            elif value == "{":
                stack.append("}")
            elif value == "[":
                stack.append("]")
            elif not stack or stack.pop() != value:
                break

        if not stack and not copyQueue: answer += 1

        queue.append(queue.popleft())

    return answer