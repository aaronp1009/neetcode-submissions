class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i in range(1, len(prices)):
            # Looking back a day, if profit, then sell
            # this works because you can buy and sell in the same day
            sell = prices[i] - prices[i-1]
            if sell > 0:
                profit += sell

        return profit 
