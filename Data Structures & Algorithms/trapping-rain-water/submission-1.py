class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        if not height:
            return result
        
        L, R = 0, len(height) - 1
        left_max, right_max = height[L], height[R]

        while L < R:
            if left_max < right_max:
                L += 1 
                left_max = max(left_max, height[L])
                result += left_max - height[L]
            else:
                R -= 1
                right_max = max(right_max, height[R])
                result += right_max - height[R]
            
        return result
