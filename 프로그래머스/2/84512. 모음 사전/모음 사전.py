def solution(word):
    answer = 0
    
    words = ["A", "E", "I", "O", "U"]
    wordList = list(word)

    length = len(word)
    
    lst = [""]
    for i in range(5):
        answer += 1
        lst[-1] = words[i]
        if lst == wordList:
            return answer
        
        lst.append("")
        for j in range(5):
            answer += 1
            lst[-1] = words[j]
            if lst == wordList:
                return answer
            
            lst.append("")
            for k in range(5):
                answer += 1
                lst[-1] = words[k]
                if lst == wordList:
                    return answer
                
                lst.append("")
                for l in range(5):
                    answer += 1
                    lst[-1] = words[l]
                    if lst == wordList:
                        return answer
                    
                    lst.append("")
                    for m in range(5):
                        answer += 1
                        lst[-1] = words[m]
                        if lst == wordList:
                            return answer
                        
                    lst = lst[:-1]
                lst = lst[:-1]
            lst = lst[:-1]
        lst = lst[:-1]


