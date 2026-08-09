class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxx = nums[0]
        for num in nums:
            curr = max(num, curr + num)
            maxx = max(maxx, curr)

        return maxx