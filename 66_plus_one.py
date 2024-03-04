# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:

    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)

        for i in range(N-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            elif i == 0:
                digits.insert(0, 1)
                i += 1

            digits[i] = 0
            
        return digits