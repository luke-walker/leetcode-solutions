# Time Complexity: O(m+n)
# Auxiliary Space: O(m)
# m = # nums, n = # nodes

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_set = set(nums)

        while head is not None and head.val in num_set:
            head = head.next

        prev, curr = head, head.next
        while curr is not None:
            if curr.val in num_set:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return head
