def solution(routes):
    answer = 0

    routes.sort()

    cur = (routes[0][0], routes[0][1])

    for idx in range(1, len(routes)):
        
        start = routes[idx][0]
        end = routes[idx][1]

        if start > cur[1]:
            answer += 1
            cur = (start, end)
        else:
            cur = (max(cur[0], start), min(cur[1], end))
        
    if cur: answer += 1

    return answer