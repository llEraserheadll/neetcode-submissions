from heapq import heappush,heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []

        for x,y in points:
            dist = -(x**2 + y**2)
            heappush(min_heap,(dist,x,y))
            if len(min_heap) > k:
                heappop(min_heap)
        
        res = []
        
        for _ in range(k):
            distance,x,y = heappop(min_heap)
            res.append((x,y))
        
        return res