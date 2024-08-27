# Time Complexity: O(n!)
# Auxiliary Space: O(n)

class Solution:
    def totalNQueens(self, n: int) -> List[List[str]]:
        def is_valid(board: List[int]) -> bool:
            n = len(board)

            for i in range(n-1):
                x1 = board[i]
                
                for j in range(i+1, n):
                    x2 = board[j]

                    if x1 == x2:
                        return False
                    if abs(x1 - x2) / (j - i) == 1.0:
                        return False

            return True

        def backtrack(current: List[int]) -> int:
            if not is_valid(current):
                return 0

            if len(current) == n:
                return 1

            result = 0
            for i in range(n):
                current.append(i)
                result += backtrack(current)
                current.pop()

            return result

        return backtrack([])
