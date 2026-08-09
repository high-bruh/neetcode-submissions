class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2

        if (2 * target) % 2:
            return False

        target = int(target)
        dp = [False] * (target + 1)
        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]
