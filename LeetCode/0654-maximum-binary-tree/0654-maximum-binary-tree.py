# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: list) -> Optional[TreeNode]:
        
        def searchMaxNumber(nums: list) -> (int, int):
            idx = 0
            num = 0
            for i in range(len(nums)):
                if num < nums[i]:
                    idx = i
                    num = nums[i]

            return (idx, num)
        
        def recursive(nums: [int]) -> TreeNode:
            if len(nums) == 1:
                return TreeNode(val=nums[0])
            if len(nums) == 0:
                return None
            
            idx, num = searchMaxNumber(nums)
            leftNode = recursive(nums[:idx])
            rightNode = recursive(nums[idx+1:])
            
            return TreeNode(val=num, left=leftNode, right=rightNode)
            
            
        treeNode = recursive(nums)
        return treeNode