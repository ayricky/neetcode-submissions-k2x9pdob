class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool: 
        NUM_ROWS, NUM_COLS = len(board[0]), len(board)

        row_map = defaultdict(set)
        col_map = defaultdict(set)
        board_map = defaultdict(set)
        for r in range(NUM_ROWS):
            for c in range(NUM_COLS):
                val = board[r][c]
                if val == '.':
                    continue

                if val in row_map[r] or val in col_map[c] or val in board_map[(r // 3 , c // 3)]:
                    return False
                
                row_map[r].add(val)
                col_map[c].add(val)
                board_map[(r //3 , c // 3)].add(val)

        return True