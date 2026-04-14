class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # if k <= 1 or len(nums) == 1:
        #     return False

        seen = set()
        L = 0

        for R in range(0, len(nums)):
            if nums[R] in seen:
                return True

            seen.add(nums[R])

            if R - L >= k:
                seen.remove(nums[L])
                L += 1
        
        return False