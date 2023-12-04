def solution(k, tangerine: list):
    answer = 0
    dict = {}

    for tan in tangerine:
        if tan in dict:
            dict[tan] += 1
        else:
            dict[tan] = 1

    sortedDict = sorted(dict.items(), key=lambda item : item[1], reverse=True)

    for key, val in sortedDict:
        k -= val
        answer += 1

        if k <= 0:
            break

    return answer