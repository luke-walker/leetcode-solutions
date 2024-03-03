// Time Complexity: O(n^2)
// Space Complexity: O(n^2)
//     Note: Can be improved to O(1) with formula

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> dp;

        for (int i = 0; i < numRows; ++i) {
            dp.push_back(vector<int>(i+1, 1));

            for (int j = 1; j < i; ++j) {
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
            }
        }

        return dp;
    }
};