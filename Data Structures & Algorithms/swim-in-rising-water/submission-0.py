from heapq import heappush,heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = [(grid[0][0],0,0)] # max_height,r,c,
        visit = set()
        visit.add((0,0))
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        rows = len(grid)
        cols = len(grid[0])

        while min_heap:
            h,row,col = heappop(min_heap)
            if row == rows - 1 and col == cols - 1 :
                return h
            for dr,dc in directions:
                r = row + dr
                c = col + dc
                if r <0 or r >= rows or c < 0 or c>= cols or (r,c) in visit:
                    continue
                visit.add((r,c))
                heappush(min_heap,(max(h,grid[r][c]),r,c))
        return None
