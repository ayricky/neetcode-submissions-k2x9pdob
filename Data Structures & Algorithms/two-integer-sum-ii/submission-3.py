class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_index = {}
        for i, num in enumerate(numbers):
            compliment = target - num
            if compliment in num_index and num_index[compliment] < i:
                return [num_index[compliment] + 1, i + 1]
            num_index[num] = i
        
        return []