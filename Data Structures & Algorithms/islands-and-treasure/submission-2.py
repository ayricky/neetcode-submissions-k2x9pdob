class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance

                directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]
                for dr, dc in directions:
                    if 0 <= dr < ROWS and 0 <= dc < COLS and (dr, dc) not in visited and grid[dr][dc] != -1:
                        visited.add((dr, dc))
                        q.append((dr, dc))

            distance += 1
                    
        # return grid