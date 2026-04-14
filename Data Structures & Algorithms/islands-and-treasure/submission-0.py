class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        def add_cell(r, c):
            if (
                min(r, c) < 0 or r == ROWS or c == COLS 
                or (r, c) in visited
                or grid[r][c] == -1
            ):
                return

            visited.add((r, c))
            queue.append((r, c))
        
        queue, visited = deque(), set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))
        
        distance = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = distance

                add_cell(r + 1, c)
                add_cell(r - 1, c)
                add_cell(r, c + 1)
                add_cell(r, c - 1)
            distance += 1




