class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 1, max(piles)
        result = max(piles)

        while lo <= hi:
            k = (lo + hi) // 2
            
            total_time = 0
            for p in piles:
                total_time += (p + k - 1) // k # ceiling division

            if total_time <= h:
                result = k
                hi = k - 1
            else:
                lo = k + 1
        
        return result