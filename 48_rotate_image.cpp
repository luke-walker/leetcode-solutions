// Time Complexity: O(n^2)
// Auxiliary Space: O(1)

class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        const int N = matrix.size();

        // Reverse matrix rows
        int l = 0;
        int r = N-1;
        while (l < r) {
            vector<int> temp = matrix[l];
            matrix[l] = matrix[r];
            matrix[r] = temp;

            ++l;
            --r;
        }
    
        // Transpose matrix
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < i; ++j) {
                int temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
    }
};