class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, i):
            if i == len(nums):
                res.append(nums[:])

            for j in range(i, len(nums)):
                nums[j], nums[i] = nums[i], nums[j]
                backtrack(nums, i + 1)
                nums[j], nums[i] = nums[i], nums[j]

        backtrack(nums, 0)
        return res



