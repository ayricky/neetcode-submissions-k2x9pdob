class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = stones
        heapq.heapify_max(max_heap)

        while len(max_heap) > 1:
            a = heapq.heappop_max(max_heap)
            b = heapq.heappop_max(max_heap)
            remaining = a - b

            if remaining > 0:
                heapq.heappush_max(max_heap, remaining)
        
        return max_heap[0] if max_heap else 0