class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, cur_set = [], []
        self.helper(0, nums, result, cur_set)
        return result
    
    def helper(self, i, nums, result, cur_set):
        if i >= len(nums):
            result.append(cur_set.copy())
            return

        cur_set.append(nums[i])
        self.helper(i+1, nums, result, cur_set)
        cur_set.pop()

        self.helper(i+1, nums, result, cur_set)
