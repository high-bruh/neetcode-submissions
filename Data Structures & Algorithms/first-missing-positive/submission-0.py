class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        has1 = False
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                has1 = True
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1

        if not has1:
            return 1

        for i in range(n):
            val = abs(nums[i])

            if val == n:
                nums[0] = -abs(nums[0])
            else:
                nums[val] = -abs(nums[val])

        for i in range(1, n):
            if nums[i] > 0:
                return i

        return n if nums[0] > 0 else n + 1
