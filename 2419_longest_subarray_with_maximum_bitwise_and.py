# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_num = max(nums)
        count = 0
        result = 0
        for num in nums:
            if num == max_num:
                count += 1
                result = max(result, count)
            else:
                count = 0

        return result
