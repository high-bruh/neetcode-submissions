class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [False] * (len(p) + 1)
        dp[len(p)] = True

        for i in range(len(s), -1, -1):
            nextdp = dp[len(p)]
            dp[len(p)] = (i == len(s))
            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")
                res = False
                if (j + 1) < len(p) and p[j + 1] == "*":
                    res = dp[j + 2]
                    if match:
                        res = dp[j] or res
                elif match:
                    res = nextdp

                nextdp = dp[j]
                dp[j] = res

        return dp[0]