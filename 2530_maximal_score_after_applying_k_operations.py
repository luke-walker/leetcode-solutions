# Time Complexity: O(n+k*log(n))
# Auxiliary Space: O(n)

import heapq
import math

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        queue = [-x for x in nums]
        heapq.heapify(queue)

        score = 0
        for _ in range(k):
            x = -heapq.heappop(queue)
            score += x
            heapq.heappush(queue, -math.ceil(x / 3))

        return score
