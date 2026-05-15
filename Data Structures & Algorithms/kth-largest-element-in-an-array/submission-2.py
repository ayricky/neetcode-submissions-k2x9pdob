class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = nums
        heapq.heapify_max(nums)

        result = max_heap[0]
        while k != 0:
            result = heapq.heappop_max(max_heap)
            k -= 1
        
        return result