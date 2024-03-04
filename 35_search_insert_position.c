// Time Complexity: O(log n)
// Auxiliary Space: O(1)

int searchInsert(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize-1;

    while (left <= right) {
        int middle = (left+right)/2;
        int num = nums[middle];

        if (num < target) {
            left = middle+1;
        } else if (num > target) {
            right = middle-1;
        } else {
            return middle;
        }
    }

    return left;
}