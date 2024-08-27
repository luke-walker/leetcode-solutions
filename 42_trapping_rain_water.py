# Time Complexity: O(n)
# Auxiliary Space: O(1)

class Solution:
    def trap(self, height: List[int]) -> int:
        left_max, right_max = 0, 0
        left_index, right_index = 0, len(height)-1
    
        result = 0
        while left_index <= right_index:
            if left_max <= right_max:
                if left_max > height[left_index]:
                    result += left_max - height[left_index]
                else:
                    left_max = height[left_index]

                left_index += 1
            else:
                if right_max > height[right_index]:
                    result += right_max - height[right_index]
                else:
                    right_max = height[right_index]

                right_index -= 1

        return result
