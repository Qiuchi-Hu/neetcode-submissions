from collections import deque

class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:
        endWord_exist = False
        neighbors = {}
        for word in wordList:
            for i in range(len(word)):
                parent = word[:i]+"*"+word[i+1:]
                if not parent in neighbors:
                    neighbors[parent] = []
                neighbors[parent].append(word)
                
            if word == endWord:
                endWord_exist = True
        
        if not endWord_exist:
            return 0
        
        transform = deque([(beginWord,1)])
        visited = set()

        while transform:
            word, step = transform.popleft()
            if word == endWord:
                return step
            visited.add(word)
            next_level = set()
            parent_list = [word[:i]+"*"+word[i+1:] for i in range(len(word))]

            for parent in parent_list:
                if parent in neighbors:
                    for w in neighbors[parent]:
                        if w not in visited:
                            next_level.add(w)
            
            next_level = list(next_level)
            for w in next_level:
                transform.append((w,step+1))

        return 0


