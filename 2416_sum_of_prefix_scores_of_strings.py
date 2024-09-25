# Time Complexity: O(n)
# Auxiliary Space: O(m+n)
# m = # of words, n = # of characters in words

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
                curr.count += 1

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        result = []
        trie = Trie(words)
        for word in words:
            total_count = 0
            curr = trie.root
            for c in word:
                curr = curr.children[c]
                total_count += curr.count
            result.append(total_count)

        return result
