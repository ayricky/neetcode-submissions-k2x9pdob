class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {')': '(', 
                ']': '[', 
                '}': '{'}
        stack = []
        for char in s:
            if len(stack) > 0:
                if char in mapper and stack[-1] == mapper[char]:
                    stack.pop()
                else:
                    stack.append(char)
            else:
                stack.append(char)
        if stack == []:
            return True
        else:
            return False

#  
#