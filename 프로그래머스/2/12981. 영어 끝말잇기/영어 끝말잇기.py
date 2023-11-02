def solution(n, words):
    
    num = 0
    turn = 0
    dict = { words[0]: True }

    for i in range(1, len(words)):
        turn = i // n + 1

        if words[i - 1][-1] != words[i][0] or words[i] in dict: 
            num = i % n + 1
            break

        dict[words[i]] = True
        turn = 0

    return [num, turn]