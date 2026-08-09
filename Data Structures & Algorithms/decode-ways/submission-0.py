class Solution:
    def numDecodings(self, s: str) -> int:
        dp2 = 0
        dp1 = 1  # Base case: an empty string has one way to be decoded

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp = 0
            else:
                dp = dp1
                if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in "0123456")):
                    dp += dp2
            dp2, dp1 = dp1, dp  # Shift the window

        return dp1
