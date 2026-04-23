class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n :
            return True
        
        map = {i:[] for i in range(n)}
        
        for u,v in edges:
            map[u].append(v)
            map[v].append(u)
        
        visit = set()
        
        def dfs(node,prev):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in map[node]:
                if nei == prev:
                    continue
                if not dfs(nei,node):
                    return False
            return True
        
        return dfs(0,-1) and n == len(visit)





