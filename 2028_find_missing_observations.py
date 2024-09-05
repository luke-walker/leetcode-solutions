# Time Complexity: O(m+n)
# Auxiliary Space: O(n)

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missing_total = (mean * (len(rolls) + n)) - sum(rolls)
        
        if missing_total < n or missing_total > n*6:
            return []

        result = []
        for _ in range(n):
            result.append(missing_total // n)
        for i in range(missing_total % n):
            result[i] += 1

        return result
