class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stk = []

        for i in range(len(heights) + 1):
            while stk and (i == len(heights) or heights[stk[-1]] >= heights[i]):
                h = heights[stk.pop()]
                w = i if not stk else i - stk[-1] - 1
                ans = max(ans,h * w)
            stk.append(i)

        return ans