# Time Complexity: O(log^2 n)
# Auxiliary Space: O(log n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def left_height(node):
            if not node:
                return 0
            return 1 + left_height(node.left)

        def right_height(node):
            if not node:
                return 0
            return 1 + right_height(node.right)
        
        left = left_height(root.left)
        right = right_height(root.right)

        if left == right:
            return 2 ** (left + 1) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)