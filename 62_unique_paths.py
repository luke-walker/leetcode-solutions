# Time Complexity: O(m*n)
# Auxiliary Space: O(m*n)

class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 if x == 0 or y == 0 else 0 for y in range(n)] for x in range(m)]

        queue = deque([(1, 1)])
        while len(queue) > 0:
            x, y = queue.pop()

            if x == m or y == n or dp[x][y] != 0:
                continue

            queue.appendleft((x+1, y))
            queue.appendleft((x, y+1))

            dp[x][y] = dp[x-1][y] + dp[x][y-1]

        return dp[m-1][n-1]