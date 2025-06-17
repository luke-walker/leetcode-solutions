# Time Complexity: O(n)
# Auxiliary Space: O(h)

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0

        max_val = 0
        for child in root.children:
            max_val = max(max_val, self.maxDepth(child))

        return 1 + max_val
