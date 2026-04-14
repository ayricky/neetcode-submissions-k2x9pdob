class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result, stack = [0] * len(temperatures), []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = i - stack_index

            stack.append((temp, i))

        
        return result

# stack = [30]
# 
# 
# 
# 
# 
