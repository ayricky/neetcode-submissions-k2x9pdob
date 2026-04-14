class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left = right = 0
        while right < n:
            nums[left] = nums[right]
            while right < n and nums[right] == nums[left]:
                right += 1
            left += 1
        return left
