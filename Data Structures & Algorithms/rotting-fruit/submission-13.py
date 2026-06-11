class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        fresh_fruit = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh_fruit += 1
        
        result = 0
        while q:
            r, c, time = q.popleft()
            result = max(result, time)

            directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
            for dr, dc in directions:
                if 0 <= dr < ROWS and 0 <= dc < COLS:
                    if grid[dr][dc] == 1:
                        grid[dr][dc] = 2
                        q.append((dr, dc, time + 1))
                        fresh_fruit -= 1


        return result if fresh_fruit == 0 else -1