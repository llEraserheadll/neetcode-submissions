class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False]*len(nums)
        res = []

        def dfs(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(path)
                    path.pop()
                    used[i] = False


        dfs([])
        return res