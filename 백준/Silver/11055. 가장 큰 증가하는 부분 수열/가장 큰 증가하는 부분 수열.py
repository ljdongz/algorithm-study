import sys

input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))

dp = [0] * N
dp[0] = nums[0]

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += nums[i]

"""
for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + nums[i])
            
위 방법이 안되는 이유는 반례 [1, 1, 1], [5, 1, 5]로 생각해보기
(첫 번째 수가 두 번째 수보다 작지 않은 경우)
위 반례의 경우 조건문에 진입하지 못하기 때문에 dp[i]에 현재 정수 값 nums[i]를 저장하지 못함
"""

print(max(dp))
