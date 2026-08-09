class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm = {i : [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            hm[crs].append(pre)

        seen = set()

        def dfs(crs):
            if crs in seen:
                return False

            if hm[crs] == []:
                return True

            seen.add(crs)
            for pre in hm[crs]:
                if not dfs(pre):
                    return False
            seen.remove(crs)
            hm[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True
