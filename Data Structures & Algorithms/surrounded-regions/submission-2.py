class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        safe = set()
        def dfs(r, c):
            if not 0 <= r < ROWS or not 0 <= c < COLS or board[r][c] != 'O' or (r, c) in safe:
                return

            safe.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for r in range(ROWS):
            for c in range(COLS):
                if r in (0, ROWS - 1) or c in (0, COLS - 1) and board[r][c] == 'O':
                    dfs(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in safe:
                    board[r][c] = 'X'
        
        return
        