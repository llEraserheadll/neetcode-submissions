from heapq import heappop,heappush
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        n = len(points)
        for i in range(n):
            x1,y1 = points[i]
            for j in range(i+1,n):
                x2,y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append((j,dist))
                adj[j].append((i,dist))
        
        visit = set()
        res = 0
        min_heap = [(0,0)]
        

        while len(visit) < n :
            d,n1 = heappop(min_heap)
            if n1 in visit:
                continue
            visit.add(n1)
            res += d
            for n2,distance in adj[n1]:
                if n2 not in visit:
                    
                    heappush(min_heap,((distance,n2)))
        return res