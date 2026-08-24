class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_count = len(board)
        col_count = len(board[0])

        current_str = []
        index = 0
        word_len = len(word)
        found = False
        moves = [[1,0],[-1,0],[0,1],[0,-1]]
        explored = set()

        def explore(r,c):
            nonlocal index,found,explored
            
            if board[r][c] == word[index]:
                if index==word_len-1:
                    found = True
                    return
                explored.add((r,c))
                index+=1
                for r_move, c_move in moves:
                    r_new = r+r_move
                    if r_new >=0 and r_new < row_count:
                        c_new = c+c_move
                        if c_new >=0 and c_new< col_count and not (r_new,c_new) in explored:
                            explore(r_new,c_new)
                            if found:
                                return
                explored.remove((r,c))
                index-=1
        
        for r in range(row_count):
            for c in range(col_count):
                explore(r,c)
                if found:
                    return True
        
        return False