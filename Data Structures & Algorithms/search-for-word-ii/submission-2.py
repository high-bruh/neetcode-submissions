from typing import List

class WordDict:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['#'] = {}  # End marker as dict

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        d = WordDict()
        for w in words:
            d.insert(w)

        ROWS, COLS = len(board), len(board[0])
        res = set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                board[r][c] not in node):
                return

            char = board[r][c]
            board[r][c] = '#'
            next_node = node[char]
            word += char

            if isinstance(next_node, dict) and '#' in next_node:
                res.add(word)

            dfs(r + 1, c, next_node, word)
            dfs(r - 1, c, next_node, word)
            dfs(r, c + 1, next_node, word)
            dfs(r, c - 1, next_node, word)
            board[r][c] = char  

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, d.trie, "")

        return list(res)
