class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for nei in adj[node]:
                dfs(nei)
            
            return
        
        visited = set()
        result = 0
        for i in range(n):
            if i in visited:
                continue

            dfs(i)
            result += 1
        
        return result