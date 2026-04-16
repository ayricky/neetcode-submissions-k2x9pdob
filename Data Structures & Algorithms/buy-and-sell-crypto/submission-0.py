class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0, 1
        max_profit = 0

        while R < len(prices):
            if prices[L] < prices[R]:
                max_profit = max(max_profit, prices[R] - prices[L])
            else:
                 L = R
            R += 1
        
        return max_profit