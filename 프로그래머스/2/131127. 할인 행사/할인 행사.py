def solution(want: list, number: list, discount: list):
    answer = 0
    dict = {}

    def init():
        for i in range(len(want)):
            dict[want[i]] = [number[i], 0]

    init()
    
    for i in range(len(discount) - 9):
        for j in range(10):
            product = discount[i+j]
            if product in dict: 
                dict[product][1] += 1

        for j in range(len(want)):
            if dict[want[j]][0] > dict[want[j]][1]:
                break
            if j == len(want) - 1:
                answer += 1
        
        init() 

    return answer