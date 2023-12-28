import heapq

def solution(scoville: list, K):
    answer = 0

    heapq.heapify(scoville)

    while(scoville[0] < K and len(scoville) > 1):
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new = first + (second * 2)

        heapq.heappush(scoville, new)

        answer += 1

    if scoville[0] >= K:
        return answer
    else: return -1