class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deps = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            deps[crs] += 1
            adj[pre].append(crs)

        finish = 0
        def dfs(node):
            nonlocal finish
            finish += 1
            deps[node] -= 1
            for nei in adj[node]:
                deps[nei] -= 1
                if deps[nei] == 0:
                    dfs(nei)

        for i in range(numCourses):
            if deps[i] == 0:
                dfs(i)
            
        return finish == numCourses




            

            
