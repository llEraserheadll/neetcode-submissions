class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        cmap = {i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            cmap[crs].append(pre)
        
        cycle = set()
        visit = set()
        result = []

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in cmap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            result.append(crs)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return result
