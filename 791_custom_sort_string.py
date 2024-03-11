# Time Complexity: O(m+n)
# Auxiliary Space: O(m+n)
# m = # of characters in order string, n = # of characters in s string

class Solution:

    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)

        res = ""

        for c in order:
            if c in counter:
                res += c * counter[c]

        for c in counter:
            if c not in order:
                res += c * counter[c]

        return res