class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        p = 0
        n = len(s)

        while p < n / 2:
            s[p], s[n - p - 1] = s[n - p - 1], s[p]
            p += 1
        