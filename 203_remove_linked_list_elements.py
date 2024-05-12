# Time Complexity: O(n)
# Auxiliary Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        last = dummy
        curr = head
        while curr:
            if curr.val == val:
                last.next = curr.next
            else:
                last = curr
            curr = curr.next

        return dummy.next