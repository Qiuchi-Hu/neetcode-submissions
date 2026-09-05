from collections import deque

class Solution:
    def ladderLength(
        self,
        beginWord: str,
        endWord: str,
        wordList: List[str]
    ) -> int:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, steps = queue.popleft()

            if word == endWord:
                return steps

            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":

                    candidate = word[:i] + ch + word[i+1:]

                    if candidate in wordSet:
                        wordSet.remove(candidate)
                        queue.append((candidate, steps + 1))

        return 0