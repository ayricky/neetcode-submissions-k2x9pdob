class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        left, right = 0, n - 1
        top, bottom = 0, n - 1
        val = 1

        while left <= right:
            # fill top
            for col in range(left, right + 1):
                matrix[top][col] = val
                val += 1
            top += 1

            # fill right
            for row in range(top, bottom + 1):
                matrix[row][col] = val
                val += 1
            right -= 1

            # fill bottom (reverse)
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = val
                val += 1
            bottom -= 1

            # fill left (reverse)
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = val
                val += 1
            left += 1
        
        return matrix