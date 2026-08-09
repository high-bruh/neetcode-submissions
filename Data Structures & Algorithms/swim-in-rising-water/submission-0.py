class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        seen = set()
        minHeap = [(grid[0][0], 0, 0)]
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        seen.add((0, 0))
        while minHeap:
            t, i, j = heapq.heappop(minHeap)
            if i == n - 1 and j == n - 1:
                return t

            for dx, dy in dirs:
                r, c = i + dx, j + dy
                if not 0 <= r < n or not 0 <= c < n or (r, c) in seen:
                    continue

                seen.add((r, c))
                heapq.heappush(minHeap, (max(t, grid[r][c]), r, c))

        
            

            

            
