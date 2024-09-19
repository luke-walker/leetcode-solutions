class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        memo = {}
        def dfs(expr: str) -> List[int]:
            if expr.isdigit():
                return [int(expr)]
            if expr in memo:
                return memo[expr]

            possible = []
            for i, c in enumerate(expr):
                if c.isdigit():
                    continue

                left = dfs(expr[:i])
                right = dfs(expr[i+1:])

                for x in left:
                    for y in right:
                        if c == "+":
                            possible.append(x+y)
                        elif c == "-":
                            possible.append(x-y)
                        elif c == "*":
                            possible.append(x*y)

            memo[expr] = possible
            return possible
                
        return dfs(expression)
