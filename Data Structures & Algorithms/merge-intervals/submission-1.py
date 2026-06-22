class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        min_heap = intervals
        heapq.heapify(min_heap)
        
        result = []
        while min_heap:
            start, end = heapq.heappop(min_heap)

            if not result:
                result.append([start, end])
            elif start <= result[-1][1]:
                if end > result[-1][1]:
                    result[-1][1] = end
            else:
                result.append([start, end])
        
        return result
            
        
