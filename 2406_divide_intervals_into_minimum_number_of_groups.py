# Time Complexity: O(n*log(n))
# Auxiliary Space: O(n)

import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        queue = []

        for start, end in intervals:
            if len(queue) > 0 and start > queue[0]:
                heapq.heappop(queue)
            heapq.heappush(queue, end)

        return len(queue)
