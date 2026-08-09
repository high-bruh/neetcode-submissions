class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[v].append(u)
            adj[u].append(v)

        seen = [False] * n

        def dfs(node):
            for nei in adj[node]:
                if not seen[nei]:
                    seen[nei] = True
                    dfs(nei)

        ans = 0
        for node in range(n):
            if not seen[node]:
                seen[node] = True
                dfs(node)
                ans += 1

        return ans       