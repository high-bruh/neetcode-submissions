class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        
        res = x
        while res * res > x:
            res = (res + x // res) // 2

        return res