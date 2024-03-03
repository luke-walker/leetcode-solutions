// Time Complexity: O(n)
// Space Complexity: O(n)

int fib(int n) {
    if (n == 0 || n == 1) {
        return n;
    }

    int* dp = malloc(sizeof(int)*n);

    dp[0] = 1;
    dp[1] = 1;

    // O(n)
    for (int i = 2; i < n; ++i) {
        dp[i] = dp[i-2] + dp[i-1];
    }

    int ans = dp[n-1];

    free(dp);

    return ans;
}