class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        s = [-1 * stone for stone in stones]
        heapq.heapify(s)
        while len(s) > 1:
            s1 = -1 * heapq.heappop(s)
            s2 = -1 * heapq.heappop(s)
            if abs(s1 - s2):
                heapq.heappush(s, -1 * abs(s1 - s2))

        return 0 if not s else -1 * s[0]