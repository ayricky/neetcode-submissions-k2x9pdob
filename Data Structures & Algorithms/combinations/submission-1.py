class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result, subset = [], []

        def backtrack(i):
            if len(subset) == k:
                result.append(subset.copy())
                return
            
            for j in range(i, n + 1):
                subset.append(j)
                backtrack(j + 1)
                subset.pop()

        backtrack(1)
        return result            
