class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n =  len(nums)
        if n <= 1:
            return

        k = k % n
        count = start = 0

        while count < n:
            curr = start
            prev = nums[start]
            while True:
                nxt = (curr + k) % n
                nums[nxt], prev = prev, nums[nxt]
                curr = nxt
                count += 1

                if start == curr:
                    break

            start += 1 