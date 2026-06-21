class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False

        adj_list = defaultdict(list)
        for a, b in edges:
            adj_list[b].append(a)
            adj_list[a].append(b)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                
                if not dfs(nei, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n