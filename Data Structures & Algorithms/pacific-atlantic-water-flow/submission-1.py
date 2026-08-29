from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        #summit = {c:0 for c in cols}

        pacific = set()
        queue = deque()
        for c in range(cols):
            queue.append((0,c))
        for r in range(1,rows):
            queue.append((r,0))

        while queue:
            r,c = queue.popleft()
            #summit[c] = max(r, summit[c])
            pacific.add((r,c))
            cur_height = heights[r][c]

            if r+1 < rows and not (r+1,c) in queue and heights[r+1][c] >= cur_height:
                queue.append((r+1,c))
            if c+1 < cols and not (r,c+1) in queue and heights[r][c+1] >= cur_height:
                queue.append((r,c+1))
            if not (r-1,c) in pacific and r-1 >= 0 and heights[r-1][c] >= cur_height:
                queue.append((r-1,c))
            if not (r,c-1) in pacific and c-1 >= 0 and heights[r][c-1] >= cur_height:
                queue.append((r,c-1))
            
            
        atlantic = set()
        for c in range(cols-1,-1,-1):
            queue.append((rows-1, c))
        for r in range(rows-2, -1, -1):
            queue.append((r, cols-1))
        
        while queue:
            r,c = queue.popleft()
            atlantic.add((r,c))
            cur_height = heights[r][c]

            if r-1 >= 0 and not (r-1,c) in queue and heights[r-1][c] >= cur_height:
                queue.append((r-1,c))
            if c-1 >= 0 and not (r,c-1) in queue and heights[r][c-1] >= cur_height:
                queue.append((r,c-1))
            if not (r,c+1) in atlantic and c+1 < cols and heights[r][c+1] >= cur_height:
                queue.append((r,c+1))
            if not (r+1,c) in atlantic and r+1 < rows and heights[r+1][c] >= cur_height:
                queue.append((r+1,c))
        
        #print("pacific: ", pacific)
        #print("atlantic: ", atlantic)
        results = pacific & atlantic
        return [[r,c] for r,c in results]
        