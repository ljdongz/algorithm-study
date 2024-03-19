import math

def solution(n, stations, w):
    answer = 0

    start = 1

    for station in stations:

        length = station - w - start

        start = station + w + 1 

        if length <= 0:
            continue

        answer += math.ceil(length / (w * 2 + 1))

    remain = n - start + 1
    if remain > 0:
        answer += math.ceil(remain / (w * 2 + 1))

    return answer