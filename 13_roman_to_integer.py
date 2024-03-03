# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def romanToInt(self, s: str) -> int:
        N = len(s)
        VALS = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        ans = 0

        for i in range(N):
            curr_c = s[i]
            ans += VALS[curr_c]

            if i+1 < N:
                next_c = s[i+1]

                if curr_c == 'I' and next_c in ['V','X']:
                    ans -= 2
                elif curr_c == 'X' and next_c in ['L','C']:
                    ans -= 20
                elif curr_c == 'C' and next_c in ['D','M']:
                    ans -= 200

        return ans