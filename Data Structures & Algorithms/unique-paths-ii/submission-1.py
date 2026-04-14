class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        cache = {}
        def dfs(r, c):
            if r > M - 1 or c > N - 1 or obstacleGrid[r][c] == 1:
                return 0
            if r == M - 1 and c == N - 1:
                return 1
            if (r, c) in cache:
                return cache[(r, c)]
            
            cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            
            return cache[(r, c)]
        
        return dfs(0, 0)