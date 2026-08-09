class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm = {i : [] for i in range(numCourses)}
        visiting = set()

        for crs, pre in prerequisites:
            hm[crs].append(pre)

        def dfs(crs):
            if crs in visiting:
                return False

            if hm[crs] == []:
                return True

            visiting.add(crs)
            for pre in hm[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            hm[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
                