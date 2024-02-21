from collections import deque

def solution(A, B):
    answer = 0

    A.sort()
    B.sort()
    B = deque(B)

    for n in A:

        while B:
            if B.popleft() > n:
                answer += 1
                break

    return answer