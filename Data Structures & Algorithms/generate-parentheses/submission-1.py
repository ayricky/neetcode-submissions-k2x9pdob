class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, subset = [], []
        def backtrack(open, closed):
            if open == closed == n :
                result.append("".join(subset))
                return
            
            if open < n:
                subset.append("(")
                backtrack(open + 1, closed)
                subset.pop()

            if closed < open:
                subset.append(")")
                backtrack(open, closed + 1)
                subset.pop()
        
        backtrack(0, 0)
        return result