class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        moves = [[0,1],[0,-1],[1,0],[-1,0]]
        rows = len(grid)
        cols = len(grid[0])

        groups = 0

        def dfs(r,c):
            nonlocal moves,grid

            if grid[r][c] == "1":
                grid[r][c] = "0"
                for r_move, c_move in moves:
                    r_new = r + r_move
                    if r_new >=0 and r_new < rows:
                        c_new = c + c_move
                        if c_new >=0 and c_new < cols:
                            dfs(r_new,c_new)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    groups+=1
                    dfs(r,c)

        
        return groups