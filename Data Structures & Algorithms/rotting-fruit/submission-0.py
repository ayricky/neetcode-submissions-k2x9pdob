class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue, visited = deque(), set()
        fresh = time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while fresh > 0 and queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    new_row, new_col = r + dr, c + dc
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1