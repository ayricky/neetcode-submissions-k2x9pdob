class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        cur_sum = 0
        min_length = float("inf")

        for R in range(len(nums)):
            cur_sum += nums[R]
            while cur_sum >= target:
                min_length = min((R - L) + 1, min_length)
                cur_sum -= nums[L]
                L += 1
        
        if min_length == float("inf"):
            return 0
        
        return min_length