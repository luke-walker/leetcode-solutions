# Time Complexity: O(n!)
# Auxiliary Space: O(n)

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
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

        result = []
        def backtrack(current: List[int]):
            if not is_valid(current):
                return

            if len(current) == n:
                result.append(current[:])
                return

            for i in range(n):
                current.append(i)
                backtrack(current)
                current.pop()
        backtrack([])

        return [[(("."*y)+"Q"+("."*(n-y-1))) for y in x] for x in result]
