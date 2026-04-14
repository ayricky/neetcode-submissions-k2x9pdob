from collections import Counter
from heapq import heapify

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        min_heap = [(count, num) for num, count in counts.items()]
        heapify(min_heap)

        while len(min_heap) > k:
            heapq.heappop(min_heap)
        
        return [x[1] for x in min_heap]
