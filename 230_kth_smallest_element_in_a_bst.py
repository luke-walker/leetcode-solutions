# Time Complexity: O(n)
# Auxiliary Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            nonlocal k

            if not node:
                return -1

            res = inorder(node.left)
            if res < 0:
                k -= 1
                if k == 0:
                    return node.val

                if node.right:
                    return inorder(node.right)

            return res

        return inorder(root)