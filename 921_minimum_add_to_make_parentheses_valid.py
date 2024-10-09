class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opening, closing = 0, 0
        for c in s:
            if c == '(':
                opening += 1
            elif c == ')':
                if opening > 0:
                    opening -= 1
                else:
                    closing += 1
        return opening + closing
