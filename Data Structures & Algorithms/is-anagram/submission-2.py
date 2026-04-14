from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = defaultdict(int)
        for char in s:
            count1[char] += 1

        count2 = defaultdict(int)
        for char in t:
            count2[char] += 1
        
        return count1 == count2