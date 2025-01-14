import sys
from collections import deque

input = sys.stdin.readline

N, K = list(map(int, input().split()))

count = {}

q = deque()

total = 0
houseCount = 0

sam = list(map(int, input().split()))
for s in sam:
  count[s] = 0
  q.append(s)

while q:
  cur = q.popleft()

  nexts = [cur - 1, cur + 1]
  for next in nexts:
    if next not in count:
      q.append(next)
      count[next] = count[cur] + 1
      total += count[next]
      houseCount += 1
      if houseCount == K: 
        q = deque()
        break

print(total)