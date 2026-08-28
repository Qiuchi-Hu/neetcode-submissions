class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def sink(r, c):
            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            count = 1

            if r > 0:
                count += sink(r - 1, c)

            if r + 1 < rows:
                count += sink(r + 1, c)

            if c > 0:
                count += sink(r, c - 1)

            if c + 1 < cols:
                count += sink(r, c + 1)

            return count

        largest = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    largest = max(largest, sink(r, c))

        return largest