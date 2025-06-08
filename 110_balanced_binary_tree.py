# Time Complexity: O(n)
# Auxiliary Space: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def dfs(x: Optional[TreeNode]) -> int:
            if not x:
                return 0

            left = dfs(x.left)
            right = dfs(x.right)
            if abs(left - right) > 1:
                nonlocal res
                res = False
                return 0

            return 1 + max(left, right)

        dfs(root)
        return res
