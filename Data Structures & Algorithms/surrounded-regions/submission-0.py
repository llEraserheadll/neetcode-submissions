class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])


        def addnew(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'
            addnew(r+1,c)
            addnew(r-1,c)
            addnew(r,c+1)
            addnew(r,c-1)

        for c in range(cols):
            if board[0][c] == 'O':
                addnew(0,c)
            if board[rows-1][c] == 'O':
                addnew(rows-1,c)
        
        for r in range(rows):
            if board[r][0] == 'O':
                addnew(r,0)
            if board[r][cols-1] == 'O':
                addnew(r,cols-1)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'