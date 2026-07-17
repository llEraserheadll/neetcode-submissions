class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        q = collections.deque()
        visit = set()

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visit and grid[r][c] == 0:
                    q.append((r,c))
                    visit.add((r,c))
        
        dist = 0

        def addnew(row,col):
            if row in range(rows) and col in range(cols) and grid[row][col] == 2147483647 and (row,col) not in visit:
                visit.add((row,col))
                q.append((row,col))
        while q:
            qlen = len(q)
            for i in range(qlen):
                r,c = q.popleft()
                grid[r][c] = dist
                addnew(r+1,c)
                addnew(r-1,c)
                addnew(r,c+1)
                addnew(r,c-1)

            dist += 1
