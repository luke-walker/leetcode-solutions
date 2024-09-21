# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        x = 1                       # start at 1
        for _ in range(n):
            result.append(x)        # add current node to result
            if x*10 > n:            # check if leaf node
                if x == n:          # check if last leaf node at max depth
                    x //= 10        # go back one level
                x += 1              # next node
                while x % 10 == 0:  # correct current node (ie 19 -> 20 should be 19 -> 2)
                    x //= 10
            else:
                x *= 10             # traverse to next level

        return result
