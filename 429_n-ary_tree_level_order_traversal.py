# Time Complexity: O(n)
# Auxiliary Space: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        queue = deque([(0, root)])
        while len(queue) > 0:
            level, node = queue.pop()
            if node is None:
                continue
            if level >= len(result):
                result.append([node.val])
            else:
                result[level].append(node.val)
            for child in node.children:
                queue.appendleft((level+1, child))

        return result
