class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            cnt = 0
            num = i
            while num:
                cnt += num & 1
                num >>= 1
            res.append(cnt)

        return res