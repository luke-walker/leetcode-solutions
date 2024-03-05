# Time Complexity: O(n)
# Auxiliary Space: O(n)

class Solution:

    def addBinary(self, a: str, b: str) -> str:
        M = len(a)
        N = len(b)

        if M > N:
            b = '0'*(M-N) + b
        elif N > M:
            a = '0'*(N-M) + a

        s = ""
        carry = 0

        for i in range(max(M, N)-1, -1, -1):
            count = int(a[i]) + int(b[i]) + carry
            carry = count // 2
            s = str(count % 2) + s
            
        return '1'*carry + s