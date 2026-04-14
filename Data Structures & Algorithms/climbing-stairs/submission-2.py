class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dfs(i):
            if i >= n:
                return i == n
            if i in cache:
                return cache[i]
            ans = dfs(i + 1) + dfs(i + 2)
            cache[i] = ans
            return ans 

        return dfs(0)