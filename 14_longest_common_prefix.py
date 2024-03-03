# Time Complexity: O(m*n)
# Auxiliary Space: O(n)
# m = # of strings, n = length of shortest string

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        for i in range(len(strs[0])):
            c = strs[0][i]

            for j in range(1,len(strs)):
                if len(strs[j]) <= i or strs[j][i] != c:
                    return ans
            
            ans += c

        return ans