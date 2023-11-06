def solution(arr: list):
    arr.sort()
    big = arr.pop()
    isContinue = True
    mul = 1
    while isContinue:
        isContinue = False
        for i in arr.__reversed__():
            if (big * mul) % i != 0:
                isContinue = True
                mul += 1
                break

        
    return big * mul