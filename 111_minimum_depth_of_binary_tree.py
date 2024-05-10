# Time Complexity: O(n)
# Auxiliary Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def minDepth(self, root: Optional[TreeNode], depth=0) -> int:
        if not root:
            return depth
        
        depth += 1

        if not root.left and not root.right:
            return depth
        elif root.left and root.right:
            return min(self.minDepth(root.left, depth), self.minDepth(root.right, depth))
    
        return self.minDepth(root.left if root.left else root.right, depth)