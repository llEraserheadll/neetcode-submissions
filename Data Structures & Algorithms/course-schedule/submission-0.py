class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        coursemap = {i:[] for i in range(numCourses) }

        for crs,pre in prerequisites:
            coursemap[crs].append(pre)
        
        visit = set()


        def dfs(crs):
            if crs in visit:
                return False
            
            if coursemap[crs] == []:
                return True
            
            visit.add(crs)
            for pre in coursemap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            coursemap[crs] = []
            return True



        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
