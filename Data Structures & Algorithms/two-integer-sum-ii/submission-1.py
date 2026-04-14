class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1

        while lo < hi:
            if numbers[lo] + numbers[hi] > target:
                hi -= 1
            elif numbers[lo] + numbers[hi] < target:
                lo += 1
            else:
                return [1 + lo, 1 + hi]