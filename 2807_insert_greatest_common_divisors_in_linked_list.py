# Time Complexity: O(n)
# Auxiliary Space: O(n)

import math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head, head.next
        while curr is not None:
            prev.next = ListNode(math.gcd(prev.val, curr.val), curr)
            prev, curr = curr, curr.next

        return head
