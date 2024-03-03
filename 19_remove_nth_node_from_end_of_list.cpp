// Time Complexity: O(n)
// Auxiliary Space: O(n)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(1), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int& n) {
        if (!head)
            return nullptr;

        head->next = removeNthFromEnd(head->next, n);

        if (n == 0) {
            ListNode* temp = head->next;

            delete head;

            return temp;
        }

        --n;

        return head;
    }
};