# Time Complexity: O(n)
# Auxiliary Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = [root]

        while len(stack) > 0:
            node = stack.pop()

            if node is None:
                continue

            result.insert(0, node.val)
            stack.extend([node.left, node.right])

        return result
