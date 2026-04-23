class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(index,path,sum):
            if sum == target:
                res.append(path[:])
                return
            
            if sum > target:
                return
            
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,path,sum + candidates[i])
                path.pop()




        backtrack(0,[],0)

        return res