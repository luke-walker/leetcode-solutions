# Time Complexity: O(m+n)
# Auxiliary Space: O(m+n)

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1 == sentence2:
            return True

        words1 = sentence1.split(" ")
        words2 = sentence2.split(" ")
        short, long = None, None
        if len(words1) < len(words2):
            short = words1
            long = words2
        else:
            short = words2
            long = words1

        m = len(short)
        n = len(long)
        left, right = 0, 0
        while left < m and short[left] == long[left]:
            left += 1
        while right < m and short[m-right-1] == long[n-right-1]:
            right += 1

        return left + right >= m
