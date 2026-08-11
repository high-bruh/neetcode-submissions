class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return

        k = k % len(nums)
        if k:
            nums[:] = nums[-k:] + nums[:len(nums) - k]
        