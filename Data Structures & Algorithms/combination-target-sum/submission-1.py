class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(index,path,sum):
            if sum == target:
                res.append(path[:])
                return
            
            if sum > target:
                return
            
            for i in range(index,len(nums)):
                path.append(nums[i])
                backtrack(i,path,sum + nums[i])
                path.pop()




        backtrack(0,[],0)

        return res