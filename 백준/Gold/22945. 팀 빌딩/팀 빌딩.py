import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

start = 0
end = N - 1
result = 0

while start < end:
    result = max(result, ((end - start - 1) * min(nums[start], nums[end])))

    if nums[start] > nums[end]:
        end -= 1
    elif nums[start] < nums[end]:
        start += 1
    else:
        if nums[start + 1] >= nums[end - 1]:
            start += 1
        else:
            end -= 1

print(result)