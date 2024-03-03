# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:

    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        
        return len(nums)