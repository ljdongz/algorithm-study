def solution(people: list, limit):
    answer = 0
    start = 0
    end = len(people) - 1

    people.sort()

    while start <= end:
        if start == end:
            answer += 1
            break
        if people[start] + people[end] <= limit:
            start += 1
        answer += 1
        end -= 1
    
    return answer