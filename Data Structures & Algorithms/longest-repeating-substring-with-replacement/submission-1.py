class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = [0] * 26
        ans = 0
        maxf = 0
        l = 0
        for r in range(len(s)):
            counter[ord(s[r]) - ord('A')] += 1
            maxf = max(maxf, counter[ord(s[r]) - ord('A')])
            while (r - l + 1) - maxf > k:
                counter[ord(s[l]) - ord('A')] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans

        