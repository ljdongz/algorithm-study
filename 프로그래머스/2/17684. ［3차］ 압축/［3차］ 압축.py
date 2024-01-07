def solution(msg):
    answer = []
    value = 0
    word = ""

    dict = {}
    for n in range(ord("A"), ord("Z") + 1):
        dict[chr(n)] = n - 64
        value = n - 64

    for m in msg:
        # word += m

        if word + m not in dict:
            value += 1
            dict[word + m] = value
            answer.append(dict[word])
            word = m
        else:
            word = word + m

    answer.append(dict[word])

    return answer