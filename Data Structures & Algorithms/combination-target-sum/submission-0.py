class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(start,path,sum):
            if sum == target:
                result.append(path[:])
                return
            
            if sum > target:
                return 
            
            for i in range(start,len(nums)):
                path.append(nums[i])
                dfs(i,path,sum + nums[i])
                path.pop()



        dfs(0,[],0)

        return result