# Time Complexity: O(n)
# Auxiliary Space: O(log n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right: # leaf node
            return bool(root.val)
        elif root.val == 2: # OR node
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else: # AND node
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)