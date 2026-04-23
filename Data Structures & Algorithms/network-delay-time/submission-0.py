from heapq import heappop,heappush
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for s,d,t in times:
            edges[s].append((d,t))
        
        min_heap = [(0,k)]
        visit = set()
        t = 0

        while min_heap:
            w1,n1 = heappop(min_heap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(t,w1)
            for n2,w2 in edges[n1]:
                if n2 not in visit:
                    heappush(min_heap,(w1+w2,n2))
        return t if len(visit) == n else -1