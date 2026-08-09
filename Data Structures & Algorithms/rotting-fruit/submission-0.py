class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        q = deque()

        def addCell(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in seen or grid[r][c] != 1:
                return False

            seen.add((r, c))
            q.append((r, c))
            nonlocal fresh
            fresh -= 1

        fresh = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    seen.add((r, c))
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        time = 0
        while q and fresh:
            for _ in range(len(q)):
                r, c = q.popleft()
                addCell(r + 1, c)
                addCell(r, c + 1)
                addCell(r - 1, c)
                addCell(r, c - 1)
            time += 1

        return -1 if fresh else time


        
            