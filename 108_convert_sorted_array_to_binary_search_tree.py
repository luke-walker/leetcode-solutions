# Time Complexity: O(n)
# Auxiliary Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)

        if n == 0:
            return None

        mid_i = n // 2
        left = nums[:mid_i]
        right = nums[mid_i+1:]

        root = TreeNode(nums[mid_i])
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)

        return root