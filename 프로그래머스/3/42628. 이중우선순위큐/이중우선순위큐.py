import heapq

def solution(operations: list):
    pqueue = []

    def heap_pop():
        heapq.heapify(pqueue)
        heapq.heappop(pqueue)

    for op in operations:
        s = op.split()
        
        if s[0] == "I":
            pqueue.append(int(s[1]))
        elif pqueue and s[1] == "-1":
            heap_pop()
        elif pqueue and s[1] == "1":
            pqueue = [i * -1 for i in pqueue]
            heap_pop()
            pqueue = [i * -1 for i in pqueue]

    if not pqueue: return [0,0]
    else: return [max(pqueue), min(pqueue)]