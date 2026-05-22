class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result, subset = [], []
        
        candidates.sort()
        def dfs(i, curr_sum):
            if curr_sum == target:
                result.append(subset.copy())
                return
            
            if i >= len(candidates) or curr_sum > target:
                return
            
            subset.append(candidates[i])
            dfs(i + 1, curr_sum + candidates[i])
            subset.pop()

            n = 1
            while i + n < len(candidates) and candidates[i] == candidates[i + n]:
                n += 1 
            dfs(i + n, curr_sum)
        
        dfs(0, 0)
        return result