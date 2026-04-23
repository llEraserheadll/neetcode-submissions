class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        
        rows = len(grid)
        cols = len(grid[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        time = 0

        while fresh > 0 and q:
            qlen = len(q)
            for i in range(qlen):
                row,col = q.popleft()
                for dr,dc in directions:
                    r = row+dr
                    c = col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r,c))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
