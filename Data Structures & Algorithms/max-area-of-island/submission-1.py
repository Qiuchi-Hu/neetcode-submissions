class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        current_area = 0
        moves = [(1,0),(0,1),(-1,0),(0,-1)]
        row_count = len(grid)
        col_count = len(grid[0])

        def dfs(r,c):
            nonlocal max_area, grid,current_area,row_count, col_count 
            
            grid[r][c]=2
            current_area+=1
            max_area = max(max_area,current_area)

            for r_move, c_move in moves:
                r_new = r+r_move
                if r_new>=0 and r_new < row_count:
                    c_new = c+c_move
                    if c_new>=0 and c_new < col_count:
                        if grid[r_new][c_new] ==1:
                            dfs(r_new,c_new)

        
        for r in range(row_count):
            for c in range(col_count):
                if grid[r][c]==1:
                    dfs(r,c)
                    current_area = 0

        return max_area                        



