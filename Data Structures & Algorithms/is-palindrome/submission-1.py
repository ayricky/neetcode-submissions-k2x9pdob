class Solution:
    def isPalindrome(self, s: str) -> bool:
        L, R = 0, len(s) - 1

        while L < R:
            while L < R and not self.is_alpha_num(s[L]) :
                L += 1
            while R > L and not self.is_alpha_num(s[R]):
                R -= 1

            if s[L].lower() != s[R].lower():
                return False

            L += 1
            R -= 1
        
        return True

    def is_alpha_num(self, char):
        return ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z') or ord('0') <= ord(char) <= ord('9')