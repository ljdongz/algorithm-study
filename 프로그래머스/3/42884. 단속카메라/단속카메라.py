def solution(routes):
    answer = 0

    routes.sort()

    cur = ()

    for start, end in routes:
        if not cur:
            cur = (start, end)
            continue

        if start > cur[1]:
            answer += 1
            cur = (start, end)
        else:
            cur = (max(cur[0], start), min(cur[1], end))
        
    if cur: answer += 1

    return answer