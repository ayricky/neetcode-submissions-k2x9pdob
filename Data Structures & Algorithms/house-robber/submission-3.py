class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if cache[i] != -1:
                return cache[i]

            loot_a = nums[i] + dfs(i + 2)
            loot_b = dfs(i + 1)
            cache[i] = max(loot_a, loot_b)

            return cache[i]
        
        dfs(0)
        return max(cache)
            