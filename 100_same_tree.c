// Time Complexity: O(n)
// Auxiliary Space: O(n)

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    if (!p || !q) {
        return !p && !q;
    }

    return (p->val == q->val) && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}