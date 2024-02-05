import heapq

def solution(n, works):
    answer = 0

    works = [work * -1 for work in works] # Max Heap 구현을 위해 각 원소에 -1을 곱함
    heapq.heapify(works)

    # works가 비어있거나, n이 0이면 종료
    while (works and n != 0):
        work = heapq.heappop(works)
        work += 1
        if work < 0:
            heapq.heappush(works, work)
        n -= 1
    
    for work in works:
        answer += work**2


    return answer
