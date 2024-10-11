# Time Complexity: O(n*log(n))
# Auxiliary Space: O(n)

import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        friend_map = sorted([i for i in range(len(times))], key=lambda x: times[x][0])
        available = [i for i in range(len(times))]
        used = []

        for i in friend_map:
            while len(used) > 0 and used[0][0] <= times[i][0]:
                _, index = heapq.heappop(used)
                heapq.heappush(available, index)

            chair = heapq.heappop(available)
            heapq.heappush(used, (times[i][1], chair))

            if i == targetFriend:
                return chair

        return -1
