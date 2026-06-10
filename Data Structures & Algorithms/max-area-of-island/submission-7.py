class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        result, visited = 0, set()
        def dfs(r, c):
            if not 0 <= r < ROWS or not 0 <= c < COLS or (r, c) in visited or grid[r][c] == 0:
                return 0

            visited.add((r, c))
            
            area = 1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)

            return area
        
        for r in range(ROWS):
            for c in range(COLS):
                result = max(result, dfs(r, c))

        return result