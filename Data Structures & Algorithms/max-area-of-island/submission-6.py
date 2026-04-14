class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (0,-1),(-1,0),(1,0)]

        def dfs(r,c):
            if not 0 <= r < ROWS or not 0 <= c < COLS or grid[r][c] == 0:
                return 0
            
            count = 1
            grid[r][c] = 0
            for dr, dc in directions:
                count += dfs(r + dr, c + dc)
            
            return count

        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    continue
                
                max_area = max(dfs(r, c), max_area)
        
        return max_area
