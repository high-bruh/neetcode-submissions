class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        p1 = m - 1
        p10 = len(nums1) - 1
        p2 = n - 1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] >= nums2[p2]:
                nums1[p1], nums1[p10] = nums1[p10], nums1[p1]
                p1 -= 1

            else:
                nums2[p2], nums1[p10] = nums1[p10], nums2[p2]
                p2 -= 1
                
            p10 -= 1

