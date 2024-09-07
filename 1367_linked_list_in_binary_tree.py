# Time Complexity: O(m*n)
# Auxiliary Space: O(m+n)
# m = # list nodes, n = # tree nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
            if head is None:
                return True

            if root is None:
                return False

            if head.val != root.val:
                return False

            return dfs(head.next, root.left) or dfs(head.next, root.right)

        stack = [root]
        while len(stack) > 0:
            node = stack.pop()

            if node is None:
                continue

            if dfs(head, node):
                return True

            stack.extend([node.left, node.right])

        return False
