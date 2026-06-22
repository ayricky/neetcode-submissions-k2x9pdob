class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        result = 0

        L = 0
        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1
            seen.add(s[R])
            result = max(result, R - L + 1)

        return result