def solution(record: list):
    answer = []
    
    idDict = {}
    printDict = {"Enter": "들어왔습니다.", "Leave": "나갔습니다."}

    for rec in record:
        lst = rec.split(" ")
        
        if lst[0] == "Enter" or lst[0] == "Change":
            idDict[lst[1]] = lst[2]

    for rec in record:
        lst = rec.split(" ")

        if not lst[0] == "Change":
            answer.append(f"{idDict[lst[1]]}님이 {printDict[lst[0]]}")
    
    return answer