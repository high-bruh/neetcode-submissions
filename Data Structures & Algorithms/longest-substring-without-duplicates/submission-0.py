class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        
        l = 0
        for r in range(len(s)):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
            else:
                seen.add(s[r])
                ans = max(ans, r - l + 1)

        return ans
        