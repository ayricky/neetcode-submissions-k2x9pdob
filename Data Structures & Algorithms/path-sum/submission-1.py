# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, target):
            if not node:
                return False
            
            new_target = target - node.val
            if not node.left and not node.right:
                return new_target == 0
            
            return dfs(node.left, new_target) or dfs(node.right, new_target)
                
        return dfs(root, targetSum)