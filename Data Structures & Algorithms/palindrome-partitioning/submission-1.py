class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(index,path):
            if index >= len(s):
                res.append(path[:])
                return 
            
            for j in range(index,len(s)):
                if self.ispali(index,j,s):
                    path.append(s[index:j+1])
                    backtrack(j+1,path)
                    path.pop()




        backtrack(0,[])
        return res

    def ispali(self,l,r,s):
        while l < r:
            if s[l] != s[r]:
                return False
            l+= 1
            r -= 1
        return True