# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        new_target = targetSum - root.val
        if not root.left and not root.right:
            return new_target == 0
        
        return self.hasPathSum(root.left, new_target) or self.hasPathSum(root.right, new_target)
        # def dfs(node, target):
        #     if not node: # not a leaf node
        #         return False
            
        #     new_target = target - node.val
        #     if not node.left and not node.right: # base case of being a leaf node
        #         return new_target == 0
            
        #     return dfs(node.left, new_target) or dfs(node.right, new_target)
        
        # return dfs(root, targetSum)