# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue, result = deque([root]), []
        while queue:
            subset = []
            for i in range(len(queue)):
                node = queue.popleft()
                subset.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            result.append(subset)

        return [subset[-1] for subset in result]