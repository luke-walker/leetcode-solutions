# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        masks = {v: 1 << i for i, v in enumerate(['a', 'e', 'i', 'o', 'u'])}

        occur = {0: -1}
        mask = 0
        result = 0
        for i, c in enumerate(s):
            if c in masks: # vowel
                mask ^= masks[c]
            if mask in occur:
                result = max(result, i-occur[mask])
            else:
                occur[mask] = i

        return result
