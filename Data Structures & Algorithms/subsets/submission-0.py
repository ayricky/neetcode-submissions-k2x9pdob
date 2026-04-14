class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result, subset = [], []
        self.helper(0, nums, result, subset)
        return result
    
    def helper(self, i, nums, result, subset):
        if i == len(nums):
            result.append(subset.copy())
            return
        
        subset.append(nums[i])
        self.helper(i + 1, nums, result, subset)

        subset.pop()
        self.helper(i + 1, nums, result, subset)

        
