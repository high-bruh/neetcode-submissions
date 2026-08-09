class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])

        dist = [float('inf') for _ in range(n)]
        dist[src] = 0
        q = [(src, 0)]

        while q and k >= 0:
            for i in range(len(q)):
                curr, cost = q.pop(0)
                for nei, price in adj[curr]:
                    if price + cost >= dist[nei]:
                        continue
                    dist[nei] = price + cost
                    q.append((nei, dist[nei]))
            k -= 1

        return -1 if dist[dst] == float('inf') else dist[dst]

