class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        cur = 0
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * (n + 1)
        cycle = set()
        cycle_start = -1

        def dfs(node, par):
            nonlocal cycle_start
            if visited[node]:
                cycle_start = node
                return True

            visited[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    if cycle_start != -1:
                        cycle.add(node)
                    if cycle_start == node:
                        cycle_start = -1
                    return True
            return False

        dfs(1, -1)

        for u, v in edges[::-1]:
            if u in cycle and v in cycle:
                return [u, v]

        return []        


        ans = []
        for i in range(n):
            if not visited[i]:
                dfs(i, -1)

        

