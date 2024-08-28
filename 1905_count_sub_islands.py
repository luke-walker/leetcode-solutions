# Time Complexity: O(m*n)
# Auxiliary Space: O(m*n)

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])

        result = 0
        visited = set()

        for i in range(m):
            for j in range(n):
                if (i, j) in visited:
                    continue

                if grid2[i][j] != 1:
                    continue

                subisland = True
                stack = [(i, j)]

                while len(stack) > 0:
                    x, y = stack.pop()

                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue

                    if grid2[x][y] != 1:
                        continue

                    if (x, y) in visited:
                        continue

                    visited.add((x, y))

                    if grid1[x][y] == 0:
                        subisland = False

                    for x_off, y_off in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        stack.append((x+x_off, y+y_off))

                if subisland:
                    result += 1

        return result
