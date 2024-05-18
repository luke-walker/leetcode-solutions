# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:

    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        res = ""

        for i in range(n*2):
            if i & 1:
                res += word2[i//2]
            else:
                res += word1[i//2]
        
        return res + (word1 if len(word1) > len(word2) else word2)[n:]