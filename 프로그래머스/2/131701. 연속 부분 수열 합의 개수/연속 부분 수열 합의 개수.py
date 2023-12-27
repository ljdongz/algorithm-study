
def solution(elements):
    answer = set()

    length = len(elements)
    elements = elements + elements
    
    for n in range(1, length + 1):
        for i in range(length):
            answer.add(sum(elements[i:i+n]))
    
    return len(answer)