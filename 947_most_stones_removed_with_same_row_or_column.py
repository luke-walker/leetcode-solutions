# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        table = {}

        def find(v: int) -> int:
            if v not in table:
                table[v] = v
                return v

            # path compression
            root = table[v]
            while root != table[root]:
                root = table[root]

            table[v] = root

            return root

        def union(x: int, y: int) -> None:
            u, v = find(x), find(y)

            if u == v:
                return

            table[u] = v

        for x, y in stones:
            union(x+1, -(y+1))

        count = 0
        for k in table:
            if k == table[k]:
                count += 1

        return len(stones) - count
