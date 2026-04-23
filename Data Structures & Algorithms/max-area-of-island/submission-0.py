class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        directions  = [[1,0],[-1,0],[0,1],[0,-1]]
        visit = set()
        area = 0


        def bfs(r,c):
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))
            res = 1

            while q:
                row,col = q.popleft()
                for dr,dc in directions:
                    r = row + dr
                    c = col + dc

                    if (r in range(rows) and c in range(cols) and grid[r][c] == 1 and (r,c) not in visit ):
                        q.append((r,c))
                        visit.add((r,c))
                        res += 1
            return res


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    area = max(area,bfs(r,c))
        
        return area