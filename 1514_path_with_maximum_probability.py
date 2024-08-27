# Time Complexity: O(E*log(V))
# Auxiliary Space: O(V+E)

from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(lambda: [])
        for i, edge in enumerate(edges):
            for node in edge:
                graph[node].append((succProb[i], edge[abs(edge.index(node)-1)]))
            
        visited = set()
        queue = [(-1, start_node)]
        while len(queue) > 0:
            prob, node = heapq.heappop(queue)

            if node == end_node:
                return -prob

            if node in visited:
                continue

            visited.add(node)

            for edge in graph[node]:
                heapq.heappush(queue, (prob*edge[0], edge[1]))

        return 0
