# Time Complexity: O(n^2 log n)
# Auxiliary Space: O(n)

class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted([x**2 for x in nums])