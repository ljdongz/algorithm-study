# 6 5 4

def solution(citations):
    citations.sort(reverse = True)
    
    for i in range(len(citations)):
        hIndex = i + 1
        if hIndex > citations[i]:
            return hIndex - 1
        
    return hIndex