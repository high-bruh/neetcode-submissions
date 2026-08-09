class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if not 0 <= r < ROWS or not 0 <= c < COLS or grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        maxx = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxx = max(maxx, dfs(r, c))

        return maxx 