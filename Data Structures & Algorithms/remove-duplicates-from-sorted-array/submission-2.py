class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique = set()

        i = 0
        while i < len(nums):
            num = nums[i]
            if num not in unique:
                unique.add(num)
            else:
                nums.pop(i)
                i -= 1
            
            i += 1

        return len(nums)