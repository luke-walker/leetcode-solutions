# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def helper(small, large):
            return [x for x in small if x in large]
        
        set1, set2 = set(nums1), set(nums2)

        if len(set1) < len(set2):
            return helper(set1, set2)
        
        return helper(set2, set1)