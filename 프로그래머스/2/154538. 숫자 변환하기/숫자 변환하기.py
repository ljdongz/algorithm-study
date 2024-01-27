from collections import deque

def solution(x, y, n):

    q = deque()
    q.append((y, 0))

    while q:
        cur_y, cur_count = q.popleft()

        if cur_y == x:
            return cur_count
        
        if cur_y % 2 == 0:
            q.append((cur_y / 2, cur_count + 1))
        if cur_y % 3 == 0:
            q.append((cur_y / 3, cur_count + 1))
        if cur_y - n >= x:
            q.append((cur_y - n, cur_count + 1))

    return - 1