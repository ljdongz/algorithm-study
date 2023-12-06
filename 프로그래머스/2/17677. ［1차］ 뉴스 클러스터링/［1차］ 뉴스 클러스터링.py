def solution(str1: str, str2: str):
    answer = 0

    arr1 = splitStr(str1)
    arr2 = splitStr(str2)
    
    if not arr1 and not arr2:
        return 1 * 65536

    a = 0
    b = 0

    inter = set(arr1) & set(arr2)
    union = set(arr1) | set(arr2)

    for s in inter:
        a += min(arr1.count(s), arr2.count(s))

    for s in union:
        b += max(arr1.count(s), arr2.count(s))

    answer = a / b
    
    return int(answer * 65536)


def splitStr(str):
    array = []

    for i in range(0, len(str) - 1):
        splitStr = ""
        for j in range(2):
            s = str[i+j].upper()

            if (ord(s) >= 65 and ord(s) <= 90):
                splitStr += s
        
        if len(splitStr) == 2:
            array.append(splitStr)

    return array