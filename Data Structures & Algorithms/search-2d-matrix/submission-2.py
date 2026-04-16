class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        rows, cols = len(matrix), len(matrix[0])
        hi, lo = 0, rows * cols - 1

        while hi <= lo:
            mid = (hi + lo) // 2
            row = mid //cols
            col = mid % cols
            val = matrix[row][col]

            if val < target:
                hi = mid + 1
            elif val > target:
                lo = mid - 1
            else:
                return True
        
        return False
    