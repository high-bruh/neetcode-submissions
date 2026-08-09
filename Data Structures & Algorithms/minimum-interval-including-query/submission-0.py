class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        ans = [0] * len(queries)
        intervals.sort(key = lambda x: x[0])
        minHeap = []
        queries = [(queries[i], i) for i in range(len(queries))]
        queries.sort(key = lambda x: x[0])
        p = 0
        for i in range(len(queries)):
            while p < len(intervals) and intervals[p][0] <= queries[i][0]:
                heapq.heappush(minHeap,(intervals[p][1] - intervals[p][0] + 1, intervals[p][1]))
                p += 1
            
            while minHeap and minHeap[0][1] < queries[i][0]:
                heapq.heappop(minHeap)
            ans[queries[i][1]] = minHeap[0][0] if minHeap else -1
        return ans

        