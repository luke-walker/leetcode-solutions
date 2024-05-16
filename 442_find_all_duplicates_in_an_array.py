# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:

    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            abs_num = abs(num)

            if nums[abs_num - 1] < 0:
                res.append(abs_num)
            else:
                nums[abs_num - 1] = -nums[abs_num - 1]

        return res