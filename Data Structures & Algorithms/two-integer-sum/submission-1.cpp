class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int n = nums.size();
        unordered_map<int, int> hm;

        for (int i = 0; i < n; i++){
            int diff = target - nums[i];
            if (hm.find(diff) != hm.end()){
                return {hm[diff], i};
            }
            hm[nums[i]] = i;
        }
        return {};
    }
};
