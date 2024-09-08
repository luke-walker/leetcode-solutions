# Time Complexity: O(n+k)
# Auxiliary Space: O(k)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # Count Nodes in List
        n = 0
        curr = head
        while curr is not None:
            n += 1
            curr = curr.next

        # Split List
        result = []
        prev, curr = None, head
        for i in range(k):
            part = curr
            
            for _ in range((n // k) + (1 if i < (n % k) else 0)):
                if curr is None:
                    break
                prev, curr = curr, curr.next

            if prev is not None:
                prev.next = None
            result.append(part)
                
        return result
