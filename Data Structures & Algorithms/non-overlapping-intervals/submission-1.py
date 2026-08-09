class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        prevEnd = intervals[0][1]
        ans = 0

        for interval in intervals[1:]:
            if interval[0] < prevEnd:
                ans += 1
            else:
                prevEnd = interval[1]

        return ans
