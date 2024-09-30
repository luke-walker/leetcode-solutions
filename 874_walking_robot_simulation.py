# Time Complexity: O(m+n)
# Auxiliary Space: O(n)
# m = # of commands, n = # of obstacles

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs_set = set([(x, y) for x, y in obstacles])
        x, y = 0, 0
        dx, dy = 0, 1
        max_distance = 0
        for cmd in commands:
            if cmd == -2:
                dx, dy = -dy, dx
            elif cmd == -1:
                dx, dy = dy, -dx
            else:
                for _ in range(cmd):
                    if (x+dx, y+dy) in obs_set:
                        break
                    x += dx
                    y += dy
                    max_distance = max(max_distance, x**2 + y**2)

        return max_distance
