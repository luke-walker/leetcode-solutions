# Time Complexity: O(m+n)
# Auxiliary Space: O(m+n)
# m = size of arr, n = size of queries

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = []
        for i, num in enumerate(arr):
            prefix.append(num ^ (prefix[i-1] if i > 0 else 0))

        result = []
        for i, j in queries:
            result.append(prefix[j] ^ (prefix[i-1] if i > 0 else 0))

        return result
