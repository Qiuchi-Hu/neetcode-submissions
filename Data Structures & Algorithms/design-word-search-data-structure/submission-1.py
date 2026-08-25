class charNode:
    def __init__(self):
        self.child = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.node = charNode()

    def addWord(self, word: str) -> None:
        cur = self.node
        for c in word:
            if not c in cur.child:
                cur.child[c] = charNode()
            cur = cur.child[c]

        cur.is_end = True
        
    def search(self, word: str) -> bool:
        any_char = "."

        def any_match(word, cur):
            nonlocal any_char
            len_word = len(word)

            for i in range(len_word):
                cur_char = word[i]
                if cur_char != any_char:
                    if not cur_char in cur.child:
                        return False
                    cur = cur.child[cur_char]
                else:
                    #print("="*30)
                    #print(cur.child.keys())
                    for c in cur.child:
                        #print(word[i+1:])
                        found = any_match(word[i+1:], cur.child[c])
                        if found:
                            return True
                    #print("recursive not found")
                    return False
            
            if cur.is_end:
                return True
            else:
                #print("cur_char",cur_char)
                return False

        return any_match(word, self.node)

        
