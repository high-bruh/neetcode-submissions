class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        l = 0
        r = row * col - 1
        while l <= r:
            m = l + (r - l) // 2
            mid = matrix[m // col][m % col]
            if mid < target:
                l = m + 1
            elif mid > target:
                r = m - 1
            else:
                return True

        return False