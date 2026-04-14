class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        queue, visited = deque(), set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))
        
        while queue:
            r, c, dist = queue.popleft()
            grid[r][c] = dist

            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            for dr, dc in directions:
                new_row, new_col = r + dr, c + dc
                if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] != -1 and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, dist + 1))
        
        return grid
