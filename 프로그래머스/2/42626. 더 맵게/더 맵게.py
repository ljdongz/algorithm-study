import heapq

def solution(scoville: list, K):
    
    hq = scoville
    heapq.heapify(hq)
    count = 0
    
    while len(hq) > 1:
        x = heapq.heappop(hq)
        y = heapq.heappop(hq)
        
        if x >= K:
            return count
        
        new = x + (y * 2)
        
        heapq.heappush(hq, new)
        count += 1
        
    scov = heapq.heappop(hq)
    
    if scov < K:
        return -1
    else:
        return count