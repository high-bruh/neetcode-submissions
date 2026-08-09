class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        minLen = min([len(s) for s in strs])

        for i in range(minLen):
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]

        return strs[0][:minLen]