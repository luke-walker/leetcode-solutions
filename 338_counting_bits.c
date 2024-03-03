// Time Complexity: O(n)
// Space Complexity: O(n)

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int n, int* returnSize) {
    *returnSize = n+1;

    int* dp = malloc(sizeof(int)*(*returnSize));

    dp[0] = 0;

    // O(n)
    for (int i = 1; i < *returnSize; ++i) {
        dp[i] = dp[i >> 1] + (i & 1);
    }

    return dp;
}