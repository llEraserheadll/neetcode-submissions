class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        

        cols = len(coins) + 1
        #basically grid is like cols are the coins that are bing used 
        #rows are the amount

        dp = [[0]*cols for _ in range(amount + 1)]
        dp[0] = [1]*cols

        for a in range(1,amount + 1):
            for i in range(len(coins) - 1,-1,-1):
                dp[a][i] = dp[a][i+1]
                if a - coins[i] >= 0:
                    dp[a][i] += dp[a - coins[i]][i]
        return dp[amount][0]
        