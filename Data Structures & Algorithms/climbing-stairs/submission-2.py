class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = {1:1,2:2}

        # def f(n):
        #     if n in memo:
        #         return memo[n]
        #     else:
        #         memo[n] = f(n-1) + f(n-2)
        #         return memo[n]
        
        # return f(n)

        if n <= 2:
            return n
        
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3,n+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[n]