# Time Complexity: O(m+n)
# Auxiliary Space: O(m)
# m = # of characters in arr1, n = # of characters in arr2

class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self, digits: List[int]):
        self.root = TrieNode()
        for digit in digits:
            curr = self.root
            for c in str(digit):
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        result = 0
        trie = Trie(arr1)
        for digit in arr2:
            count = 0
            curr = trie.root
            for c in str(digit):
                if c not in curr.children:
                    break
                curr = curr.children[c]
                count += 1

            result = max(result, count)

        return result
