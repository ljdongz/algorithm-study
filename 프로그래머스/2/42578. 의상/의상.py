def solution(clothes):
    result = 1
    dict = {}
    for i in clothes:
        if i[1] in dict:
            dict[i[1]] += 1
        else:
            dict[i[1]] = 0
    
    for val in dict.values():
        result += (val + 1) * result

    return result - 1