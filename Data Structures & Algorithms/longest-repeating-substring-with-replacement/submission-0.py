from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = Counter()
        L = result = max_frequency = 0
        
        for R in range(len(s)):
            counts[s[R]] += 1
            max_frequency = max(max_frequency, counts[s[R]])

            while (R - L + 1) - max_frequency > k:
                counts[s[L]] -= 1
                L += 1
            
            result = max(result, R - L + 1)
            
        return result