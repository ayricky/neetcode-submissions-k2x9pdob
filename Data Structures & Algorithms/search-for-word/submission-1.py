class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i, visited):
            if not (0 <= r < ROWS and 0 <= c < COLS) or (r, c) in visited:
                return False
                
            if board[r][c] != word[i]:
                return False
            
            if i == len(word) - 1:
                return True

            visited.add((r, c))

            if (dfs(r + 1, c, i + 1, visited) or
                dfs(r - 1, c, i + 1, visited) or
                dfs(r, c + 1, i + 1, visited) or
                dfs(r, c - 1, i + 1, visited)):
                return True
            
            visited.remove((r, c))
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0, set()):
                        return True
        
        return False 
