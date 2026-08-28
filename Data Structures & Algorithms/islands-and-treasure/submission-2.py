from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows = len(grid)
        cols = len(grid[0])
        
        bfs = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==0:
                    bfs.append((r,c))
        
        while bfs:
            r,c = bfs.popleft()
            next_step = grid[r][c]+1
            if r+1 < rows and grid[r+1][c] > next_step:
                grid[r+1][c] = next_step
                bfs.append((r+1,c))
            if r-1 >= 0 and grid[r-1][c] > next_step:
                grid[r-1][c] = next_step
                bfs.append((r-1,c))
            if c+1 < cols and grid[r][c+1] > next_step:
                grid[r][c+1] = next_step
                bfs.append((r,c+1))
            if c-1 >= 0 and grid[r][c-1] > next_step:
                grid[r][c-1] = next_step
                bfs.append((r,c-1))

        

            
        