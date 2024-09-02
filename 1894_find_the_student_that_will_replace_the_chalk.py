# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalk_left = k % sum(chalk)

        while chalk_left > 0:
            for i, v in enumerate(chalk):
                chalk_left -= v

                if chalk_left < 0:
                    return i

        return 0
