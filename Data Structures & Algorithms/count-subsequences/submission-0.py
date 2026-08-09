class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        if s == t:
            return 1

        def dfs(i, curr):
            if curr == t:
                return 1

            if i >= len(s):
                return 0

            return dfs(i + 1, curr + s[i]) + dfs(i + 1, curr)

        return dfs(0, '')