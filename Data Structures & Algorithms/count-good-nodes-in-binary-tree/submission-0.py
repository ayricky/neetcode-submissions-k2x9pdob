# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0

            result = 1 if node.val >= max_val else 0
            result += dfs(node.left, max(max_val, node.val))
            result += dfs(node.right, max(max_val, node.val))

            return result 
        
        return dfs(root, root.val)
