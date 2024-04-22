
def solution(sequence, k):

    result = [len(sequence)-1, len(sequence)-1]

    sum = sequence[-1]

    while result[0] >= 0:
        if sum > k:
            sum -= sequence[result[1]]
            result[1] -= 1
        elif sum < k:
            result[0] -= 1
            sum += sequence[result[0]]
        else: break

    if sequence[result[0]] == sequence[result[1]]:
        idx = 0
        while sequence[result[0]] == sequence[result[0] - (idx+1)] and result[0] - (idx+1) >= 0:
            idx += 1
        if result[0] == result[1]:
            result = [result[0] - idx, result[0] - idx]
        else:
            result = [result[0] - idx, result[1]- idx]
    
    return result
