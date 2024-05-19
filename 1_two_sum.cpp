// Time Complexity: O(n)
// Auxiliary Space: O(n)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        
        for (int i = 0; i < nums.size(); ++i) {
            int x = target - nums[i];

            if (map.contains(x)) {
                return {i, map[x]};
            }

            map.insert(make_pair(nums[i], i));
        }

        return {};
    }
};