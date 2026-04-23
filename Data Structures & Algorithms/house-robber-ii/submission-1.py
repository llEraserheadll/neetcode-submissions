class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        return max(self.robber(nums[1:]),self.robber(nums[:-1]))
    
    def robber(self,arr):

        if not arr:
            return 0
        if len(arr) == 1:
            return arr[0]
        n = len(arr)

        dp = [0]*n
        dp[0] = arr[0]
        dp[1] = max(arr[0],arr[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1],dp[i-2] + arr[i])
        
        return dp[n-1]

        