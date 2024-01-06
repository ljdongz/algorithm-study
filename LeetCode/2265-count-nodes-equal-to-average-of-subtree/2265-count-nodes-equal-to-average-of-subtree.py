# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        global count
        count = 0
        
        def postorder(root) -> (int, int):
            if root is None:
                return (0, 0)
            
            global count
            
            leftTotalValue, leftTotalCount = postorder(root.left)
            rightTotalValue, rightTotalCount = postorder(root.right)
            
            totalValue = leftTotalValue + rightTotalValue + root.val
            totalCount = leftTotalCount + rightTotalCount + 1
            
            if root.val == (totalValue // totalCount):
                count += 1

            return (totalValue, totalCount)
        
        postorder(root)
        
        return count