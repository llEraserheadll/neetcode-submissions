class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(start,path,sum):
            if sum == target:
                res.append(path[:])
                return
            
            if sum > target:
                return
            
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])
                dfs(i + 1,path,sum + candidates[i])
                path.pop()

        dfs(0,[],0)
        return res