
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

nums = list(map(int, input().split()))
nums.sort()

result = []
memo = {}

def backtrack(start, curr): # idx: 사용한 인덱스 리스트
    if len(curr) == M:
        if tuple(curr) not in memo:
            result.append(curr[:])
            memo[tuple(curr)] = True
        return
    
    for i in range(start, len(nums)):
        curr.append(nums[i])
        backtrack(i+1, curr)
        curr.pop()
        

backtrack(0, [])

for res in result:
    for r in res:
        print(r, end=" ")
    print()


