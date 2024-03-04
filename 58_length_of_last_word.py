# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:

    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])