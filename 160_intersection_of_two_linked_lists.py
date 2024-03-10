# Time Complexity: O(n)
# Auxiliary Space: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visited = set()

        while headA or headB:
            if headA:
                if headA in visited:
                    return headA

                visited.add(headA)
                headA = headA.next

            if headB:
                if headB in visited:
                    return headB

                visited.add(headB)
                headB = headB.next

        return None 