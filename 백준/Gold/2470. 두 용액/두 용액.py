import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))
nums.sort()

start = 0
end = len(nums) - 1
result = [1000000000, 1000000000]

while start < end:
    old = sum(result)
    new = nums[start] + nums[end]
    
    if abs(new) < abs(old):
        result = [nums[start], nums[end]]

    if new < 0:
        start += 1
    else:
        end -= 1

print(result[0], result[1])
    