class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdiag = set()
        negdiag = set()

        board = [['.']*n for _ in range(n)]
        res = []

        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                
                board[r][c] = 'Q'
                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)

                backtrack(r+1)

                board[r][c] = '.'
                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)




        backtrack(0)
        return res