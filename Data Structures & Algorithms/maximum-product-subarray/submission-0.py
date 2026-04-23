class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minsum = 1
        maxsum = 1
        res = nums[0]

        for n in nums:
            if n == 0:
                minsum = 1
                maxsum = 1
            tmp = maxsum*n
            maxsum = max(n,minsum*n,maxsum*n)
            minsum = min(n,tmp,minsum*n)
            res = max(res,maxsum)
        
        return res

