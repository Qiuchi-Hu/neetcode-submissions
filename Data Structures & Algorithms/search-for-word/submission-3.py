class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):
            # word 全部匹配完成
            if index == len(word):
                return True

            # 越界 / 字符不匹配
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[index]
            ):
                return False

            # 标记当前格子已使用
            original = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # 回溯：恢复现场
            board[r][c] = original

            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False