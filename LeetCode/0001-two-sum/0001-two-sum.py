class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        start = 0
        end = len(nums) - 1

        newNums = []
        for idx, num in enumerate(nums):
            newNums.append((num, idx))

        newNums.sort()

        while start < end:
            sum = newNums[start][0] + newNums[end][0]

            if sum == target:
                return [min(newNums[start][1], newNums[end][1]), max(newNums[start][1], newNums[end][1])]
            elif sum > target:
                end -= 1
            elif sum < target:
                start += 1