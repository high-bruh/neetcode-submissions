class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = [[] for _ in range(n + 1)]
        for u, v, t in times:
            adj[u].append((v, t))

        min_times = {}
        min_heap = [(0, k)] 

        while min_heap:
            time, i = heapq.heappop(min_heap)
            if i in min_times:
                continue
            min_times[i] = time
            for nei, t in adj[i]:
                if nei not in min_times:
                    heapq.heappush(min_heap, (time + t, nei))

        if len(min_times) != n:
            return -1

        return max(min_times.values())