class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hm = {}
        for i in range(len(s) - 1, -1, -1):
            if s[i] not in hm:
                hm[s[i]] = i
            
        ans = []
        l, r = 0, 0
        start = l

        while r < len(s) and l < len(s):
            r = max(hm[s[l]], r)
            if l == r:
                ans.append(l - start + 1)
                l += 1
                start = l
            else:
                l += 1


        return ans
