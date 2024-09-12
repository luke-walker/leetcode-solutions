# Time Complexity: O(n)
# Auxiliary Space: O(m)
# m = # characters in allowed, n = total # characters in words

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        letters = set(allowed)
        result = 0
        for word in words:
            consistent = True
            for letter in word:
                if letter not in letters:
                    consistent = False
                    break

            if consistent:
                result += 1

        return result
