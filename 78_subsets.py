# Time Complexity: O(2^n)
# Auxiliary Space: O(2^n)

class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        res = []

        for i in range(2**N):
            subset = []

            for j in range(i.bit_length()):
                if (i >> j) & 1:
                    subset.append(nums[j])

            res.append(subset)
           
        return res