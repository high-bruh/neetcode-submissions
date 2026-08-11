class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}     # value => index

        for i in range(len(nums)):
            if nums[i] in hm and abs(hm[nums[i]] - i) <= k:
                return True

            hm[nums[i]] = i
            
        return False
