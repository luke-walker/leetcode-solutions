# Time Complexity: O(n)
# Auxiliary Space: O(n)

class TreeNode:
    def __init__(self, start, end, left=None, right=None):
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class MyCalendar:
    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        def insert(root: TreeNode) -> Tuple[Optional[TreeNode], bool]:
            if root is None:
                return TreeNode(start, end), True

            if end <= root.start:
                root.left, success = insert(root.left)
                return root, success
            elif start >= root.end:
                root.right, success = insert(root.right)
                return root, success

            return root, False

        self.root, success = insert(self.root)
        return success

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
