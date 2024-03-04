# Time Complexity: O(n log n)
# Auxiliary Space: O(n)

class Solution:

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens = collections.deque(sorted(tokens))

        score, best = 0, 0

        while len(tokens) > 0:
            if tokens[0] <= power:
                power -= tokens.popleft()
                score += 1
                best = max(best, score)
            elif score >= 1:
                power += tokens.pop()
                score -= 1
            else:
                break

        return best