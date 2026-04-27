class Solution:
    # find pivot ; binary search both halves of pivor
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1
        
        pivot = lo

        def binary_search(lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    return mid
            return -1
        
        left = binary_search(0, pivot - 1)
        if left != -1:
            return left
        
        return binary_search(pivot, len(nums) - 1) 
