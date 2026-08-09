class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie
        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]
        d['#'] = '#'  # End of word marker

    def search(self, word: str) -> bool:
        def dfs(j, root):
            d = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for val in d.values():
                        if val != '#' and dfs(i + 1, val):
                            return True
                    return False
                else:
                    if c not in d:
                        return False
                    d = d[c]
            return '#' in d

        return dfs(0, self.trie)
