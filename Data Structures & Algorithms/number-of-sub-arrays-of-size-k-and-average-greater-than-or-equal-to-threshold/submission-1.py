class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = k * threshold
        current_sum = result = 0

        L = 0
        for R in range(len(arr)):
            current_sum += arr[R]
            window_size = R - L + 1
            
            if window_size >= k:
                if current_sum >= target_sum:
                    result += 1
                    
                current_sum -= arr[L]
                L += 1

        
        return result