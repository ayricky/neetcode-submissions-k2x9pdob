class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1), (0,-1),(-1,0),(1,0)]
        visited = set()

        def dfs(r,c):
            if not 0 <= r < ROWS or not 0 <= c < COLS or grid[r][c] == 0 or (r, c) in visited:
                return 0
            
            visited.add((r, c))
            count = 1
            for dr, dc in directions:
                count += dfs(r + dr, c + dc)
            
            return count

        area = 0
        for r in range(ROWS):
            for c in range(COLS):                
                area = max(dfs(r, c), area)
        
        return area
