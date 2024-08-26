# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        result = [asteroids[0]]

        for asteroid in asteroids[1:]:
            remaining = asteroid

            while len(result) > 0 and result[-1] > 0 and asteroid < 0:
                top = result.pop()

                if abs(top) == abs(asteroid):
                    remaining = None
                    break
                elif abs(top) > abs(asteroid):
                    remaining = top
                    break

            if remaining is not None:
                result.append(remaining)

        return result
