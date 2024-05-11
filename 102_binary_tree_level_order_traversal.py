# Time Complexity: O(n)
# Auxiliary Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([(root, 0)])

        while len(queue) > 0:
            curr, level = queue.pop()

            if not curr:
                continue

            if len(res) == level:
                res.append([curr.val])
            else:
                res[level].append(curr.val)

            queue.appendleft((curr.left, level + 1))
            queue.appendleft((curr.right, level + 1))

        return res