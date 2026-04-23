class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod = 1
        minprod = 1
        res = nums[0]

        for num in nums:
            if num == 0:
                minprod = 1
                maxprod = 1

            tmp = num*maxprod
            
            maxprod = max(num,maxprod*num,minprod*num)
            minprod = min(num,tmp,minprod*num)
            res = max(res,maxprod)
        
        return res