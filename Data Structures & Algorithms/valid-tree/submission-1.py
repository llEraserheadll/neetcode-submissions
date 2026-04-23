class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #basically a cycle check
        visit = set()
        cmap = collections.defaultdict(list)
        for u,v in edges:
            cmap[u].append(v)
            cmap[v].append(u)
        
        q = collections.deque()
        q.append((0,-1))
        visit.add(0)

        while q:
            node,parent = q.popleft()
            for nei in cmap[node]:
                if nei == parent:
                    continue
                if nei not in visit:
                    q.append((nei,node))
                    visit.add(nei)
                else:
                    return False
        return len(visit) == n