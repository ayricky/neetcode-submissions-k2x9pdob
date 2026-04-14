class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area, visited = 0, set()

        def dfs(r, c):
            if not (0 <= r < ROWS) or not (0 <= c < COLS) or grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))       
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area