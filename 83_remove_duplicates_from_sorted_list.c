// Time Complexity: O(n)
// Auxiliary Space: O(1)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    if (!head) {
        return head;
    }

    struct ListNode* slow = head;
    struct ListNode* fast = head->next;

    while (fast) {
        if (slow->val == fast->val) {
            struct ListNode* temp = fast;

            fast = fast->next;
            slow->next = fast;

            free(temp);
        } else {
            slow = slow->next;
            fast = fast->next;
        }
    }

    return head;
}