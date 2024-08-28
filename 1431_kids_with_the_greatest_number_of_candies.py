# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)

        result = []
        for kid in candies:
            result.append(kid + extraCandies >= max_candies)

        return result
