class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i in range(1, len(prices)):
            # Look back one day before, see if the sale is positive
            sale = prices[i] - prices[i-1]
            if sale > 0:
                profit += sale
        
        return profit
