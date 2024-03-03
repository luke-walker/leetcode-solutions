# Time Complexity: O(m*n)
# Auxiliary Space: O(1)
# m = length of 'haystack' string, n = length of 'needle' string

class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        M = len(haystack)
        N = len(needle)

        for i in range(M-N+1):
            found = True

            for j in range(N):
                if haystack[i+j] != needle[j]:
                    found = False
                    break

            if found:
                return i
            
        return -1
    
""" 
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
"""