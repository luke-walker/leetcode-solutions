# Time Complexity: O(n)
# Auxiliary Space: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = []
        stack = [root]

        while len(stack) > 0:
            node = stack.pop()

            result.insert(0, node.val)
            if node.children is not None:
                stack.extend(node.children)

        return result
