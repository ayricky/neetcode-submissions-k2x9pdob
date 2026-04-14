class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        total_product = 1
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total_product *= num
        
        if zero_count > 1:
            return result

        for i, num in enumerate(nums):
            if zero_count == 1:
                if num == 0:
                    result[i] = total_product
            else:
                result[i] = total_product // num
        
        return result
        