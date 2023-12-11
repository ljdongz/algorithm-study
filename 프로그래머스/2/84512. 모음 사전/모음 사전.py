def solution(word):
    answer = 0

    words = ["A", "E", "I", "O", "U", ""]

    wordsDict = {}
    wordsList = []

    for i in words:
        for j in words:
            for k in words:
                for l in words:
                    for m in words:
                        w = i+j+k+l+m
                        if w not in wordsDict: wordsDict[w] = True

    
    for k, v in wordsDict.items():
        wordsList.append(k)

    wordsList.sort()
    return wordsList.index(word)