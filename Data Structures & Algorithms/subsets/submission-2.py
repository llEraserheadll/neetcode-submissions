class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        

        res = []
        
        def backtrack(index,path):
            res.append(path[:])

            for i in range(index,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()





        backtrack(0,[])
        return res