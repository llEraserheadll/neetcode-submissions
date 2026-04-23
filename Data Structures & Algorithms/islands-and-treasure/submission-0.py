from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])
        dq = deque()
        visit = set()


        def addnew(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or (r,c) in visit or grid[r][c] == -1:
                return
            visit.add((r,c))
            dq.append((r,c))


        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    dq.append((r,c))
        
        dist = 0

        while dq:
            qlen = len(dq)
            for i in range(qlen):
                r,c = dq.popleft()
                grid[r][c] = dist
                addnew(r+1,c)
                addnew(r-1,c)
                addnew(r,c+1)
                addnew(r,c-1)

            dist += 1
