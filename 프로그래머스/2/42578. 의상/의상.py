def solution(clothes):
    result = 1
    dict = {}
    
    for cloth in clothes:
        if cloth[1] in dict:
            dict[cloth[1]] += 1
        else:
            dict[cloth[1]] = 1
    
    for value in dict.values():
        result *= (value + 1)
        
    return result - 1