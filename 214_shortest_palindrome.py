# Time Complexity: O(n^2)
# Auxiliary Space: O(n)

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        rev = s[::-1]
        for i in range(n):
            if s[:n-i] == rev[i:]:
                return rev[:i] + s

        return ""
