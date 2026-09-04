class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        o = "O"
        visited = "#"
        def dfs(r,c):
            nonlocal board
            board[r][c] = visited
            if r+1 < rows and board[r+1][c] == o:
                dfs(r+1,c)
            if r-1>=0 and board[r-1][c] == o:
                dfs(r-1,c)
            if c-1>=0 and board[r][c-1] == o:
                dfs(r,c-1)
            if c+1<cols and board[r][c+1] == o:
                dfs(r,c+1)
        
        borders = [(0,c) for c in range(cols)]
        borders.extend([(r,0) for r in range(rows)])
        borders.extend([(rows-1,c) for c in range(cols)])
        borders.extend([(r,cols-1) for r in range(rows)])

        for r,c in borders:
            if board[r][c]==o:
                dfs(r,c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == o:
                    board[r][c] = "X"
                elif board[r][c] == visited:
                    board[r][c] = o