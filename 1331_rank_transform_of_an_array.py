# Time Complexity: O(n*log(n))
# Auxiliary Space: O(n)

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(arr)
        rank = {}

        for x in sorted_arr:
            if x not in rank:
                rank[x] = len(rank) + 1

        return [rank[x] for x in arr]
