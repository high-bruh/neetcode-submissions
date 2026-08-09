class Solution:
    def jump(self, nums: List[int]) -> int:
        gas = 0
        ans = 0
        curr = 0
        for num in nums:
            if curr >= len(nums) - 1:
                return ans
            if num > gas:
                gas = num
                ans += 1
                curr += gas
                if curr >= len(nums) - 1:
                    return ans
            gas -= 1
        return ans



            