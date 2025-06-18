# Time Complexity: O(n)
# Auxiliary Space: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue

            res.append(node.val)
            stack.extend(list(reversed(node.children)))

        return res
