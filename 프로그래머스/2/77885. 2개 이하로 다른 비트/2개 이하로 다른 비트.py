def convertToBin(n):
    if n == 0: return [0]

    result = [0] * 50
    i = 0
    while n != 0:
        result[i] = n % 2
        i += 1
        n //= 2

    return result

def convertToInt(bins):
    result = 0
    length = len(bins)-1
    for idx, b in enumerate(bins):
        result += b * (2 ** (length-idx))
    return result


def solution(numbers):
    answer = []
    
    for num in numbers:
        reverseBin = convertToBin(num)

        for i in range(len(reverseBin)):
            if reverseBin[i] == 0:
                reverseBin[i] = 1
                if i != 0 and reverseBin[i-1] == 1:
                    reverseBin[i-1] = 0
                break

        reverseBin.reverse()
        answer.append(convertToInt(reverseBin))

    return answer