# Time Complexity: O(m*n)
# Auxiliary Space: O(m*n)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        dp = {}
        def dfs(x: int, y: int)-> int:
            key = (x, y)

            if key in dp:
                return dp[key]

            longest = 0

            for x_off, y_off in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x_new, y_new = x+x_off, y+y_off

                if x_new < 0 or x_new >= m or y_new < 0 or y_new >= n:
                    continue

                if matrix[x_new][y_new] <= matrix[x][y]:
                    continue

                longest = max(longest, dfs(x+x_off, y+y_off))

            dp[key] = longest + 1

            return dp[key]

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))

        return result
