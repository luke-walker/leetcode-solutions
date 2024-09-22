# Time Complexity: O(log(n))
# Auxiliary Space: O(1)

class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def num_nodes(x: int) -> int:
            nodes = 0
            y = x + 1
            while x <= n:
                nodes += min(y, n+1) - x
                x *= 10
                y *= 10

            return nodes

        x = 1
        k -= 1
        while k > 0:
            nodes = num_nodes(x)
            if nodes <= k:
                k -= nodes
                x += 1
            else:
                k -= 1
                x *= 10

        return x
