class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        tree = {}
        stop = "*"
        visited = "."
        rows = len(board)
        cols = len(board[0])
        for word in words:
            cur = tree
            for c in word:
                if c in cur:
                    cur = cur[c]
                else:
                    cur[c] = {}
                    cur = cur[c]
            cur[stop] = 1
        
        def dfs(r,c,parent_tree, prefix):
            cur_char = board[r][c]
            
            #print("="*50)
            #print("r: ", r, "c: ",c)
            
            prefix = prefix + cur_char
            #print(prefix)
            cur_tree = parent_tree[cur_char]

            postfix = []
            if stop in cur_tree:
                if len(cur_tree)==1:
                    parent_tree.pop(cur_char)
                    return [prefix]
                else:
                    cur_tree.pop(stop)
                    postfix.append(prefix)
            
            board[r][c] = visited
            if r+1< rows and board[r+1][c] in cur_tree:
                postfix.extend(dfs(r+1,c,cur_tree,prefix))
                #print("r+1: ",postfix)
            if r-1>=0 and board[r-1][c] in cur_tree:
                postfix.extend(dfs(r-1,c,cur_tree,prefix))
                #print("r-1: ",postfix)
            if c+1< cols and board[r][c+1] in cur_tree:
                postfix.extend(dfs(r,c+1,cur_tree,prefix))
                #print("c+1: ",postfix)
            print(board[r][c-1])
            if c-1>=0 and board[r][c-1] in cur_tree:
                postfix.extend(dfs(r,c-1,cur_tree,prefix))
                #print("c-1: ",postfix)
            
            board[r][c] = cur_char
            if not len(cur_tree):
                parent_tree.pop(cur_char)

            return postfix
        
        existing_words = []
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in tree:
                    existing_words.extend(dfs(r,c,tree,""))
        
        #print(board)
        return existing_words
        


            

                
            
            


        


        