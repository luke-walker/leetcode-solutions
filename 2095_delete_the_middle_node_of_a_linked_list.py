# Time Complexity: O(n)
# Auxiliary Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        last = None
        slow = head
        fast = head

        while fast and fast.next:
            last = slow
            slow = slow.next
            fast = fast.next.next

        if last:
            last.next = slow.next

        return head