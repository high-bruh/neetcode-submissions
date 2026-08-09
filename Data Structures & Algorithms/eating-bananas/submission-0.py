class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r

        while l <= r:
            k = l + (r - l) // 2

            time = 0
            for pile in piles:
                time += math.ceil(float(pile) / k)
            
            if time <= h:
                ans = k
                r = k - 1
            else:
                l = k + 1

        return ans
        

            
    