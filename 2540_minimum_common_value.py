# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        M, N = len(nums1), len(nums2)
        i1, i2 = 0, 0

        while i1 < M and i2 < N:
            num1, num2 = nums1[i1], nums2[i2]

            if num1 < num2:
                i1 += 1
            elif num1 > num2:
                i2 += 1
            else:
                return num1

        return -1