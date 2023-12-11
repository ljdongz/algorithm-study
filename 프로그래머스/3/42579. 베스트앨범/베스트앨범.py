def solution(genres: list, plays: list):
    answer = []

    totalPlaydict = {}
    playDict = {}

    for i in range(len(genres)):
        if genres[i] in totalPlaydict:
            totalPlaydict[genres[i]] += plays[i]
            playDict[genres[i]].append((i, plays[i]))
        else:
            totalPlaydict[genres[i]] = plays[i]
            playDict[genres[i]] = [(i, plays[i])]

    totalPlaydict = sorted(totalPlaydict.items(), key=lambda item: item[1], reverse=True)

    for key, _ in totalPlaydict:
        lst = playDict[key]
        lst.sort(key=lambda x: x[1], reverse=True)
        for i in range(min(2, len(lst))):
            answer.append(lst[i][0])
    
    
    return answer