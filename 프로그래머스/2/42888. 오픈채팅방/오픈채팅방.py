def solution(record: list):
    answer = []
    dummy = []
    idDict = {}

    for rec in record:
        lst = rec.split(" ")
        
        if lst[0] == "Enter":
            idDict[lst[1]] = lst[2]
            dummy.append(f"{lst[1]}/님이 들어왔습니다.")
        elif lst[0] == "Leave":
            dummy.append(f"{lst[1]}/님이 나갔습니다.")
        elif lst[0] == "Change":
            idDict[lst[1]] = lst[2]

    for dum in dummy:
        lst = dum.split("/")
        answer.append(idDict[lst[0]] + lst[1])
    
    return answer