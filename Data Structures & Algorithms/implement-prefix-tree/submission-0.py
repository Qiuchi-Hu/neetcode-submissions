class TreeNode:
    def __init__(self):
        self.child = {}
        self.is_end = False

class PrefixTree:

    def __init__(self):
        self.child = {}
        
    def insert(self, word: str) -> None:
        trace = self.child
        len_word = len(word)
        for i in range(len_word):
            current = word[i]
            if not current in trace:
                trace[current] = TreeNode()
            trace = trace[current]
            if i == len_word-1:
                trace.is_end = True
                continue
            trace = trace.child

    def search(self, word: str) -> bool:
        len_word = len(word)
        trace = self.child
        for i in range(len_word):
            current = word[i]
            if current not in trace:
                return False
            if i == len_word -1 and not trace[current].is_end:
                return False
            trace = trace[current].child
        
        return True
        

    def startsWith(self, prefix: str) -> bool:
        len_word = len(prefix)
        trace = self.child
        for i in range(len_word):
            current = prefix[i]
            if current not in trace:
                return False
            trace = trace[current].child
        
        return True
        
        