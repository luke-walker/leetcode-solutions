# Time Complexity: O(n)
# Auxiliary Space: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        stack = []

        def dfs(node, val=0):
            if not node:
                return
            
            stack.append(node.val)
            val += node.val

            if not node.left and not node.right and val == targetSum:
                res.append(stack[:])
            else:
                dfs(node.left, val)
                dfs(node.right, val)
            
            stack.pop()
            
        dfs(root)
        return res