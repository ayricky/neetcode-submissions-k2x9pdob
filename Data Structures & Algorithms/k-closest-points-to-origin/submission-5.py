class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap, result = [], []
        
        for x, y in points:
            distance = math.sqrt(abs((0 - x)**2 + (0 - y)**2))
            heapq.heappush(min_heap, (distance, [x, y]))
        
        while len(result) < k:
            _, coord = heapq.heappop(min_heap)
            result.append(coord)

        return result