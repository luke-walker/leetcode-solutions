# Time Complexity: O(m^2+n)
# Auxiliary Space: O(m+n)
# m = length of s, n = # of characters in dictionary

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self, words: List[str]):
        self.root = TrieNode()
        for word in words:
            curr = self.root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        trie = Trie(dictionary)
        dp = {}
        
        def dfs(idx: int) -> int:
            if idx == n:
                return 0
            if idx in dp:
                return dp[idx]
            
            result = 1 + dfs(idx+1)
            curr = trie.root
            for i in range(idx, n):
                c = s[i]
                if c not in curr.children:
                    break
                curr = curr.children[c]
                if curr.word:
                    result = min(result, dfs(i+1))

            dp[idx] = result
            return result
        
        return dfs(0)
