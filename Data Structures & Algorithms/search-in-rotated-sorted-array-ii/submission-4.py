class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return True

            if nums[l] == nums[m] and nums[m] == nums[r]:
                l += 1
                r -= 1
                continue

            if target < nums[m]:
                if nums[l] <= nums[m] and target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            else:
                if nums[m] <= nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1

        return False

            

            
