# Time Complexity: O(n)
# Auxiliary Space: O(1)
# n = max # bits

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        result = 0
        for i in range(max(start.bit_length(), goal.bit_length())):
            if (start >> i) & 1 != (goal >> i) & 1:
                result += 1

        return result
