
import sys, heapq

input = sys.stdin.readline

N = int(input())
pq = []

for _ in range(N):
    n = int(input())

    if n == 0:
        if not pq:
            print(0)
        else:
            print(heapq.heappop(pq)[1])
    else:
        heapq.heappush(pq, (abs(n), n))