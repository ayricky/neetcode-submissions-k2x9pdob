class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()
        fresh_fruit = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh_fruit += 1

        if fresh_fruit == 0:
            return 0

        res = 0
        while q:
            r, c, minutes = q.popleft()
            res = minutes
            
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1 and (nr, nc) not in visited:
                    q.append((nr, nc, minutes + 1))
                    visited.add((nr, nc))
                    fresh_fruit -= 1

        return res if fresh_fruit == 0 else -1
