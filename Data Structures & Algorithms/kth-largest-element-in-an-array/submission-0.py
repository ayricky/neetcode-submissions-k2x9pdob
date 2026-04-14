class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1 * num for num in nums]
        heapq.heapify(nums)
        while k > 0:
            ans = heapq.heappop(nums) * -1
            k -= 1
        
        return ans