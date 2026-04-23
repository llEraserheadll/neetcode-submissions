from heapq import heappush,heappop
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num < -self.max_heap[0]:
            heappush(self.max_heap,-num)
        else:
            heappush(self.min_heap,num)
        
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = heappop(self.max_heap)
            heappush(self.min_heap,-val)
        
        if len(self.min_heap) > len(self.max_heap):
            value = heappop(self.min_heap)
            heappush(self.max_heap,-value)
        

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0])/2.0 + (self.min_heap[0]) / 2.0
        else:
            return (-self.max_heap[0])
        
        