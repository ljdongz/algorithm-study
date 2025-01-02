def solution(topping):
    answer = 0

    ltopping = {} # 토핑 존재 여부만 확인
    rtopping = {} # 각 토핑의 개수 확인

    lcount = 0
    rcount = 0

    for top in topping:
        if top not in rtopping:
            rtopping[top] = 1
            rcount += 1
        else:
            rtopping[top] += 1

    for top in topping:
        if top not in ltopping:
            ltopping[top] = True
            lcount += 1

        rtopping[top] -= 1
        if rtopping[top] == 0:
            rcount -= 1

        if lcount == rcount:
            answer += 1
        
    return answer

