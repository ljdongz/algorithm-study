import heapq

### min heap ###
min_heap = [5, 3, 9, 4, 1, 2, 6]

heapq.heapify(min_heap)
print(min_heap) # [1, 3, 2, 4, 5, 9, 6]

value = heapq.heappop(min_heap)
print(min_heap) # [2, 3, 6, 4, 5, 9]
print(value) # 1

heapq.heappush(min_heap, 1)
print(min_heap) # [1, 3, 2, 4, 5, 9, 6]


### max heap ###
### 각 배열 값에 -1을 곱하면서 min_heap을 사용해서 max_heap을 구현 ###
max_heap = [5, 3, 9, 4, 1, 2, 6]
max_heap = [i*-1 for i in max_heap]

heapq.heapify(max_heap)
print(max_heap) # [-9, -4, -6, -3, -1, -2, -5]

value = -1 * heapq.heappop(max_heap)
print(max_heap) # [-6, -4, -5, -3, -1, -2]
print(value) # 9

heapq.heappush(max_heap, 9 * -1)
print(max_heap) # [-9, -4, -6, -3, -1, -2, -5]
