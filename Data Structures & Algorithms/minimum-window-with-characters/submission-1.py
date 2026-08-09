class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        count = defaultdict(int)
        for c in t:
            count[c] += 1

        ans = ""
        
        l = 0
        for r in range(len(t)):
            count[s[r]] -= 1
        r = len(t) - 1

        while r < len(s):
            while all([val <= 0 for val in count.values()]):
                if not ans:
                    ans = s[l:r + 1]
                else:
                    ans = ans if len(ans) < len(s[l:r + 1]) else s[l:r + 1]
                if l < len(s):
                    count[s[l]] += 1
                l += 1
            r += 1
            if r < len(s):
                count[s[r]] -= 1

        # if all([val <= 0 for val in count.values()]):
        #     if not ans:
        #         ans = s[l:r + 1]
        #     else:
        #         ans = ans if len(ans) < len(s[l:r + 1]) else s[l:r + 1]

        return ans


            
