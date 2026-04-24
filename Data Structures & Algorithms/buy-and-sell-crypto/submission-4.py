class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 1

        if k >= len(prices) // 2:
            profit = 0
            for i in range(1,len(prices)):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
        
        n = len(prices)
        sell = [0]*n
        buy = [float('inf')]*n

        for price in prices:
            for i in range(1,k+1):
                buy[i] = min(buy[i],price-sell[i-1])
                sell[i] = max(sell[i],price - buy[i])
        
        return sell[k]

