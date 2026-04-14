class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area, visited = 0, set()

        def dfs(r, c):
            nonlocal area
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r, c) in visited:
                return
            
            visited.add((r, c))
            area += 1

            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        for r in range(rows):
            for c in range(cols):
                area = 0
                if grid[r][c] == 1 and (r, c) not in visited:
                    dfs(r, c)
                    max_area = max(max_area, area)

        return max_area