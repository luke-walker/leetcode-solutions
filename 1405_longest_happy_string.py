# Time Complexity: O(n)
# Auxiliary Space: O(n)

import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        queue = []
        if a > 0:
            heapq.heappush(queue, (-a, "a"))
        if b > 0:
            heapq.heappush(queue, (-b, "b"))
        if c > 0:
            heapq.heappush(queue, (-c, "c"))

        result = []
        while len(queue) > 0:
            x1, c1 = heapq.heappop(queue)

            if len(result) >= 2 and result[-1] == c1 and result[-1] == result[-2]: # invalid char
                if len(queue) == 0:
                    break

                x2, c2 = heapq.heappop(queue)
                result.append(c2)

                if x2+1 < 0:
                    heapq.heappush(queue, (x2+1, c2))
                
                heapq.heappush(queue, (x1, c1))
            else:
                result += c1

                if x1+1 < 0:
                    heapq.heappush(queue, (x1+1, c1))

        return "".join(result)
