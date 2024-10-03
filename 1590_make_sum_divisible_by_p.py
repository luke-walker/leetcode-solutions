# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem = sum(nums) % p
        if rem == 0:
            return 0

        result = len(nums)
        prefix_sum = 0
        rem_map = {0: -1}
        for i, num in enumerate(nums):
            prefix_sum += num
            prefix_rem = prefix_sum % p

            key = (prefix_rem - rem) % p
            if key in rem_map:
                result = min(result, i-rem_map[key])

            rem_map[prefix_rem] = i
            
        return result if result < len(nums) else -1
