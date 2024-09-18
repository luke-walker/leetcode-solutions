# Time Complexity: O(n*log(n))
# Auxiliary Space: O(n)

from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a: str, b: str) -> int:
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0

        num_strs = list(map(str, nums))
        num_strs.sort(key=cmp_to_key(cmp))

        if num_strs[0] == "0":
            return "0"

        return "".join(num_strs)
