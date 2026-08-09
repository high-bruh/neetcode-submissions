class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = cur = 0
        prefixSum = {0 : 1}

        for num in nums:
            cur += num
            diff = cur - k

            res += prefixSum.get(diff, 0)
            prefixSum[cur] = 1 + prefixSum.get(cur, 0)

        return res