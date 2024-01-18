def solution(land):

    total = land[0]

    # 행
    for i in range(1, len(land)):
        newArr = land[i]

        # 현재 행의 각 열을 방문
        for j in range(4):
            maximum = 0

            # 총 합을 구한 행에서 각 열을 방문
            for k in range(4):
                if j == k:
                    continue
                if maximum < total[k]:
                    maximum = total[k]
            
            newArr[j] += maximum
        total = newArr
  
    return max(total)