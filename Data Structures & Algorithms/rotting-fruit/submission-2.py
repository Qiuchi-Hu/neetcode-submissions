from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        rotten = deque()
        fresh_count = 0

        initial_rotten = 2
        fresh_fruit = 1

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == initial_rotten:
                    rotten.append((r,c))
                if grid[r][c] == fresh_fruit:
                    fresh_count +=1

        min_step = 0
        
        while rotten:
            #print(rotten)
            r,c = rotten.popleft()
            cur_count = fresh_count
            next_min = grid[r][c]+1
            if r+1<rows and grid[r+1][c]==fresh_fruit:
                grid[r+1][c] = next_min
                rotten.append((r+1,c))
                fresh_count-=1
            if r-1>=0 and grid[r-1][c]==fresh_fruit:
                grid[r-1][c] = next_min
                rotten.append((r-1,c))
                fresh_count-=1
            if c+1<cols and grid[r][c+1]==fresh_fruit:
                grid[r][c+1] = next_min
                rotten.append((r,c+1))
                fresh_count-=1
            if c-1>=0 and grid[r][c-1]==fresh_fruit:
                grid[r][c-1] = next_min
                rotten.append((r,c-1))
                fresh_count-=1
            
            #print(rotten)
            if fresh_count < cur_count:
                min_step = next_min - initial_rotten
            
        if fresh_count == 0:
            return min_step
        else:
            return -1
