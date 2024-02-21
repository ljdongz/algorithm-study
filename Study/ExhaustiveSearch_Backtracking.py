
"""
백트래킹(backtraking)
- 좁은 의미
    solution이 될 가능성이 없는 후보는 더 이상 탐색하지 않고 포기(backtrack)하면서 탐색
- 넓은 의미
    재귀를 이용하여 모든 경우의 수를 방문하는 것
"""

# 조합
def permute(nums):
    def backtrack(curr):
        if len(curr) == len(nums):
            ans.append(curr[:]) # 복사
            return
        
        for num in nums:
            if num not in curr:

                # 중요 포인트
                curr.append(num)
                backtrack(curr)
                curr.pop()

    ans = []
    backtrack([])
    return ans

print(permute([1,2,3])) # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]



# 순열
def combination(nums, k):
    result = []

    def backtraking(start, curr):
        if len(curr) == k:
            result.append(curr[:]) # 복사
            return
        
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtraking(i+1, curr)
            curr.pop()

    backtraking(0, [])
    return result


print(combination([1,2,3,4], 2)) # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]



# 부분집합
def subset(nums):

    result = []

    def backtraking(curr, start):
        if len(curr) == k:
            result.append(curr[:])
            return
        
        for i in range(start, len(nums)):
            curr.append(nums[i])
            backtraking(curr, i+1)
            curr.pop()

    for k in range(len(nums)+1):
        backtraking([], 0)

    return result

print(subset([1,2,3,4])) # [[], [1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]



# two sum
def twoSum(nums, k, target):
    def backtrack(start, curr):
        if len(curr) == k and sum(curr) == target:
            return curr

        for i in range(start, len(nums)):
            curr.append(nums[i])
            ret = backtrack(i+1, curr)

            if ret != None:
                return ret
            
            curr.pop()

        return None
    
    return backtrack(0, [])

print(twoSum([4,9,7,5,1], 3, 15)) # [9, 5, 1]