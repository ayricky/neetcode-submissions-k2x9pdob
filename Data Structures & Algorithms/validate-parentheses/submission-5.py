class Solution:
    def isValid(self, s: str) -> bool:
        paren_map = {'{':'}', '[':']', '(': ')'}

        stack = []
        for char in s:
            if char in paren_map:
                stack.append(paren_map[char])
            elif not stack:
                return False
            else:
                expected = stack.pop()
                if char != expected:
                    return False

        return not stack