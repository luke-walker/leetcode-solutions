# Time Complexity: O(k*n)
# Auxiliary Space: O(n)

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        result = ""

        # alpha position
        for c in s:
            result += str(ord(c) - 96)

        # transform
        for _ in range(k):
            sum_digits = 0
            for c in result:
                sum_digits += int(c)
            result = str(sum_digits)

        return int(result)
