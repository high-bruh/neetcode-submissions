class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        cache = {}

        def get(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]

        l, r = 1, n - 2
        while l <= r:
            m = (l + r) >> 1
            left, mid, right = get(m - 1), get(m), get(m + 1)
            if left < mid < right:
                l = m + 1
            elif left > mid > right:
                r = m - 1
            else:
                break
        peak = m

        def binary_search(l, r, ascending):
            while l <= r:
                m = (l + r) >> 1
                val = get(m)
                if val == target:
                    return m
                if ascending == (val < target):
                    l = m + 1
                else:
                    r = m - 1
            return -1

        res = binary_search(0, peak, True)
        return res if res != -1 else binary_search(peak, n - 1, False)