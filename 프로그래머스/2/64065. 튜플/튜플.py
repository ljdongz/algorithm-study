def solution(s: str):
    answer = []
    d:dict = {}

    s = s.replace("{", "").replace("}", "").split(",")

    for val in s:
        if val in d:
            d[val] += 1
        else:
            d[val] = 1

    d = sorted(d.items(), key = lambda item: item[1], reverse=True)

    for dic in d:
        answer.append(int(dic[0]))

    return answer