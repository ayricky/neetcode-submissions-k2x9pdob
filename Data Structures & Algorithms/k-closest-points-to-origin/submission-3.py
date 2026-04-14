from math import sqrt
import heapq

class Solution:
    def distance_from_origin(self, a, b):
        return sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))
        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for coord in points:
            distance = self.distance_from_origin(coord, (0,0))
            heapq.heappush(heap, (distance, coord))

        ans = []
        while k > 0:
            dist, point = heapq.heappop(heap)
            ans.append(point)
            k -= 1
        
        return ans
        