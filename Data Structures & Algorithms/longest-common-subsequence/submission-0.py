class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text2)
        n = len(text1)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = 0

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

        return dp[n - 1][m - 1]