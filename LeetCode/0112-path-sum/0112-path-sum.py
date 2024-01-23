

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        
        if root is None:
            return False
        
        q = deque()
        q.append((root, targetSum))

        while q:
            cur_node, cur_target = q.popleft()

            if not cur_node.left and not cur_node.right and cur_node.val == cur_target:
                return True

            if cur_node.left:
                q.append((cur_node.left, cur_target - cur_node.val))
            if cur_node.right:
                q.append((cur_node.right, cur_target - cur_node.val))
            
        return False