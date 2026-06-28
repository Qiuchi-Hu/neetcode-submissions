class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_buckets = [[0]*10 for _ in range(9)]
        col_buckets = [[0]*10 for _ in range(9)]
        sub_box_buckets = [[0]*10 for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == ".":
                    continue
                
                num = int(board[r][c])
                if row_buckets[r][num] > 0:
                    print("row",c)
                    return False
                else:
                    row_buckets[r][num]=1
                
                if col_buckets[c][num] > 0:
                    print("col",c)
                    return False
                else:
                    col_buckets[c][num]=1

                sub_box_num = 3 * (r//3) + (c//3)
                #print("num box",sub_box_num, r, c)
                if sub_box_buckets[sub_box_num][num] > 0:
                    #print("sub box", sub_box_num)
                    #print("row",r)
                    #print("col",c)
                    return False
                else:
                    sub_box_buckets[sub_box_num][num]=1

        return True

                