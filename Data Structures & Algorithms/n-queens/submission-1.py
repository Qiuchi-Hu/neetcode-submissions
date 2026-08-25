class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ph = "#"
        queen = "Q"
        empty = "."

        queen_count = n
        #board = [["#" for _ in range(n)] for _ in range(n)]
        combinations = []
        #queen_positions = []
        current_queens = []

        def explored(r,c):
            nonlocal queen_count, combinations, current_queens, empty,queen

            '''
            if (r,c) in queen_positions:
                return
            '''

            for q_r, q_c in current_queens:
                if q_r == r or q_c == c or abs(q_r-r) == abs(q_c-c):
                    return

            current_queens.append((r,c))
            queen_count-=1

            if queen_count == 0:
                board = [[empty for _ in range(n)] for _ in range(n)]
                #print(board)
                for q_r, q_c in current_queens:
                    board[q_r][q_c] = queen
                board = ["".join(row) for row in board]
                combinations.append(board)
                #queen_positions.extend(current_queens)
            elif r < n-1:
                for i in range(n):
                    explored(r+1,i)
                
            current_queens.pop()
            queen_count+=1
        
        for i in range(n):
            explored(0,i)
        
        #print(combinations)
        return combinations

                