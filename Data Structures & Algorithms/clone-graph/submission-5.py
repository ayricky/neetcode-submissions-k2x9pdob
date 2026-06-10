"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        copy_map = {}

        def dfs(node):
            if node in copy_map:
                return copy_map[node]

            copy_map[node] = Node(node.val)
            for nei in node.neighbors:
                copy_map[node].neighbors.append(dfs(nei))
            
            return copy_map[node]
        
        dfs(node)
        return copy_map[node]