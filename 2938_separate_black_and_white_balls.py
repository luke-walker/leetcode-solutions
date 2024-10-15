# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        count = 0
        result = 0
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                count += 1
            elif s[i] == '1':
                result += count

        return result
