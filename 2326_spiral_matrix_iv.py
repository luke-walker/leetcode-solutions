# Time Complexity: O(m*n)
# Auxiliary Space: O(m*n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]

        off = 0
        d = (0,1)
        x, y = 0, 0
        for _ in range(m*n):
            if head is None:
                break

            matrix[x][y] = head.val
            head = head.next

            if d == (0,1) and y+off == n-1: # right wall
                d = (1,0)
            elif d == (1,0) and x+off == m-1: # lower wall
                d = (0,-1)
            elif d == (0,-1) and y-off == 0: # left wall
                d = (-1,0)
                off += 1
            elif d == (-1,0) and x-off == 0: # upper wall
                d = (0,1)

            x, y = x+d[0], y+d[1]

        return matrix
