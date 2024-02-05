from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        q = deque(skill)
        isValid = True
        
        for s in skill_tree:
            if s in q and q.popleft() != s:
                isValid = False
                break
        
        if isValid:
            answer += 1

    return answer
