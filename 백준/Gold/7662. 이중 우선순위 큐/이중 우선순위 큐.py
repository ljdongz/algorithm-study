
import sys, heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())

    maxPQ = []
    minPQ = []
    popped = [False] * k

    for i in range(k):
        c, n = list(map(str, input().split()))
        
        # 삽입
        if c == "I":
            heapq.heappush(minPQ, (int(n), i))
            heapq.heappush(maxPQ, (int(n) * -1, i))
        # 삭제
        else:
            # 최솟값 삭제
            if n == "-1":
                while minPQ and popped[minPQ[0][1]]:
                    heapq.heappop(minPQ)
                if minPQ:
                    n, j = heapq.heappop(minPQ)
                    popped[j] = True
            # 최댓값 삭제
            else:
                while maxPQ and popped[maxPQ[0][1]]:
                    heapq.heappop(maxPQ)
                if maxPQ:
                    n, j = heapq.heappop(maxPQ)
                    popped[j] = True
    
    
    while minPQ and popped[minPQ[0][1]]:
        heapq.heappop(minPQ)
    while maxPQ and popped[maxPQ[0][1]]:
        heapq.heappop(maxPQ)

    if not maxPQ and not minPQ:
        print("EMPTY")
    elif maxPQ and not minPQ:
        print(f"{maxPQ[0][0] * -1} {maxPQ[0][0] * -1}")
    elif minPQ and not maxPQ:
        print(f"{minPQ[0][0]} {minPQ[0][0]}")
    else:
        print(f"{maxPQ[0][0] * -1} {minPQ[0][0]}")