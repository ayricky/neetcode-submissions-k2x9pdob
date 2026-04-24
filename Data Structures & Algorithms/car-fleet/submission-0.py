class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for pos, speed in sorted(zip(position, speed))[::-1]:
            time = (target - pos) / speed
            stack.append((time))

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
                



