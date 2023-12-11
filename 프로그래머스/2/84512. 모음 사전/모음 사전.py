def solution(word):
    answer = 0

    words = ["A", "E", "I", "O", "U", ""]

    wordsList = []

    for i in words:
        for j in words:
            for k in words:
                for l in words:
                    for m in words:
                        w = i+j+k+l+m
                        if w not in wordsList: wordsList.append(w)

    wordsList.sort()
    return wordsList.index(word)