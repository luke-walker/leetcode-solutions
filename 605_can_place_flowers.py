# Time Complexity: O(m)
# Auxiliary Space: O(1)

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)

        count = 0
        for i in range(m):
            if flowerbed[i] == 1:
                continue
            if i > 0 and flowerbed[i-1] == 1:
                continue
            if i < m-1 and flowerbed[i+1] == 1:
                continue

            flowerbed[i] = 1
            count += 1

        return count >= n
