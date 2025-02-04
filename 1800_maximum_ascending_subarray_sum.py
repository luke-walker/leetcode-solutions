# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        curr_sum = 0
        prev_num = 0
        for num in nums:
            if num <= prev_num:
                result = max(result, curr_sum)
                curr_sum = num
            else:
                curr_sum += num
            prev_num = num
        return max(result, curr_sum)
