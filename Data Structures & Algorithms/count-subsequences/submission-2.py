class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        if s == t:
            return 1

        dp = [0] * (len(t) + 1)
        dp[-1] = 1

        for i in range(len(s) - 1, -1, -1):
            prev = 1
            for j in range(len(t) -1, -1, -1):
                res = dp[j] + (prev if s[i] == t[j] else 0)
                prev = dp[j]
                dp[j] = res

        return dp[0]