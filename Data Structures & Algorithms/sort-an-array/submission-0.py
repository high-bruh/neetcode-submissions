class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def partition(self, nums, l, r):
        m = (l + r) >> 1
        nums[m], nums[l + 1] = nums[l + 1], nums[m]

        if nums[l] > nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
        if nums[l + 1] > nums[r]:
            nums[l + 1], nums[r] = nums[r], nums[l + 1]
        if nums[l] > nums[l + 1]:
            nums[l + 1], nums[l] = nums[l], nums[l + 1] 

        pivot = nums[l + 1]
        i = l + 1
        j = r

        while True:
            while True:
                i += 1
                if not nums[i] < pivot:
                    break
            while True:
                j -= 1
                if not nums[j] > pivot:
                    break

            if i > j:
                break

            nums[i], nums[j] = nums[j], nums[i]

        nums[l + 1], nums[j] = nums[j], nums[l + 1]
        return j

    def quickSort(self, nums, l, r):
        if r <= l + 1:
            if r == l + 1 and nums[r] < nums[l]:
                nums[l], nums[r] = nums[r], nums[l]
            return

        j = self.partition(nums, l, r)
        self.quickSort(nums, l, j - 1)
        self.quickSort(nums, j + 1, r)


        
