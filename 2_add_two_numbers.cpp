/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        return addTwoNumbers(l1, l2, false);
    }

    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2, bool carry) {
        if (!l1 && !l2) {
            if (carry) 
                return new ListNode(1);

            return nullptr;
        }

        int num = 0;

        if (l1)
            num += l1->val;
        if (l2)
            num += l2->val;
        if (carry)
            ++num;

        carry = (num >= 10);
        num %= 10;

        ListNode* head = new ListNode(num);
        head->next = addTwoNumbers(l1 ? l1->next : nullptr, l2 ? l2->next : nullptr, carry);

        return head;
    }
};