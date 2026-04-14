class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_map = {'{': '}', '[': ']', '(': ')'}

        stack = []
        for char in s:
            if char in parenthesis_map:
                stack.append(char)
            elif not stack:
                return False
            else:
                opening = stack.pop()
                if parenthesis_map[opening] != char:
                    return False 
        
        return True if not stack else False


