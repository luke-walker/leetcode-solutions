# Time Complexity: O(m+n)
# Auxiliary Space: O(m+n)
# m = # words in s1, n = # words in s2

from collections import Counter

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = Counter(s1.split(" ") + s2.split(" "))

        return [x for x in words if words[x] == 1]
