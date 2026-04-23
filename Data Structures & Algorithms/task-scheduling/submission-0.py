from heapq import heapify,heappush,heappop
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        map = Counter(tasks)
        max_heap = [-cnt for cnt in map.values()]
        heapify(max_heap)
        q = deque()
        time = 0

        while q or max_heap:
            time += 1

            if max_heap:
                count = heappop(max_heap)
                count += 1
                if count != 0:
                    cooldown = time + n
                    q.append((count,cooldown))
            
            if q and q[0][1] == time:
                heappush(max_heap,q.popleft()[0])
        return time