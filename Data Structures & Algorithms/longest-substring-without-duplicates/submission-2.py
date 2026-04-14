class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = longest = 0
        seen = set()

        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            longest = max((R - L) + 1, longest)
            seen.add(s[R])
        
        return longest
