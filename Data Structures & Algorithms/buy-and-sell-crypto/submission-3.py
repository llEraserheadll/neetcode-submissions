class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        k = 1

        if k >= n // 2:
            profit = 0
            for i in range(1,n):
                
                if prices[i]> prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
        
        buy = [float('inf')]*n
        sell = [0]*n

        for price in prices:
            for i in range(1,k+1):
                buy[i] = min(buy[i],price-sell[i-1])
                sell[i] = max(sell[i],price - buy[i])
        return sell[k]