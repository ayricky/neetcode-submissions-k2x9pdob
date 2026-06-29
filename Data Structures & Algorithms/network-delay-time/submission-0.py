class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for src, dst, weight in times:
            adj[src].append((dst, weight))
        
        dist = {node: float("inf") for node in range(1, n + 1)}
        
        def dfs(node, time):
            if time >= dist[node]:
                return
            
            dist[node] = time
            for nei, weight in adj[node]:
                dfs(nei, time + weight)
        

        dfs(k, 0)
        result = max(dist.values())
        return result if result < float('inf') else -1
