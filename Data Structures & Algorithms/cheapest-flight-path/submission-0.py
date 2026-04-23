
from heapq import heappush,heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for u,v,weight in flights:
            adj[u].append((v,weight))
        
        min_heap = [(0,src,-1)]
        
        INF = float('inf')
        dist = [[INF]*(k+5) for i in range(n)]
        dist[src][0] = 0

        while min_heap:
            cst,arp,stops = heappop(min_heap)

            if arp == dst:
                return cst
            
            if stops == k or dist[arp][stops+1]<cst:
                continue
            
            for nei,cost in adj[arp]:
                newcst = cst + cost
                newstps = stops + 1
                if dist[nei][newstps+1] > newcst:
                    dist[nei][newstps+1] = newcst
                    heappush(min_heap,(newcst,nei,newstps))
            
        return -1
