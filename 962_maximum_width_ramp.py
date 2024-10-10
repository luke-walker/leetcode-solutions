# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)

        # Create decreasing monotonic stack
        stack = [0]
        for i in range(1, n):
            if len(stack) == 0 or nums[i] <= nums[stack[-1]]:
                stack.append(i)

        # Find max ramp length
        result = 0
        for i in range(n-1, -1, -1):
            while len(stack) > 0 and nums[i] >= nums[stack[-1]]:
                result = max(result, i-stack[-1])
                stack.pop()

        return result
