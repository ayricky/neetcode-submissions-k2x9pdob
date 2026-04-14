class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        queue.append((0, 0, 0))
        visited.add((0, 0, 0))

        while queue:
            row, col, length = queue.popleft()
            if row == ROWS - 1 and col == COLS - 1:
                return length
            
            neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in neighbors:
                new_row, new_col = row + dr, col + dc
                if min(new_row, new_col) < 0 or new_row == ROWS or new_col == COLS or (new_row, new_col) in visited or grid[new_row][new_col] == 1:
                    continue
                queue.append((new_row, new_col, length + 1))
                visited.add((new_row, new_col))
        
        return  -1
